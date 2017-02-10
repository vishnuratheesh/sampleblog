
var app = angular.module('baseApp', ['restangular', 'ui.router']);



app.factory('readNextService', function(Restangular){
	
	var factory = {};
	
	factory.get = function(callback){	
		return Restangular.all('read_next/').getList();
	}
	
	return factory;
});

app.controller('articleListCtrl', function($scope, $http, Restangular) {
	
	
	Restangular.all('articles').getList().then(function(articles){
		$scope.articles = articles;
		var randomIndex = Math.floor(Math.random() * $scope.articles.length);
		$scope.main_article = $scope.articles[randomIndex];
		$("#hero-img").backstretch($scope.main_article.hero_image);
		
	});
	
	
	
});



app.controller('articleDetailCtrl', function($scope, $http,  $stateParams, Restangular) {
	
	console.log("article detail controller. article value: ");
	Restangular.one('articles', $stateParams.slug).get().then(function(article){
		$scope.article = article;
		$("#hero-img").backstretch(article.hero_image);
	   if(article.extra_image != null){
		   $("#extra-img").backstretch(article.extra_image)
	   } 
	
		
	})
	
});



app.config(function($httpProvider, RestangularProvider, $stateProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
    
    RestangularProvider.setBaseUrl('/api/v1');
    
 // add a response intereceptor
    RestangularProvider.addResponseInterceptor(function(data, operation) {
      var extractedData;
      //
      if (operation === "getList") {
        extractedData = data.objects;
        
      } else {
        extractedData = data;
      }
      return extractedData;
    });
    
    var articleListState = {
	    name: 'articlelist',
	    url: '',
	    templateUrl: 'article-list.html/',
        controller: 'articleListCtrl'
	    
	  }
	
	  var articleDetailState = {
	    name: 'article-detail',
	    url: '/articles/{slug}/',
	    templateUrl: 'article-detail.html/',
    	controller: 'articleDetailCtrl'
	    	
	  }
	
	  $stateProvider.state(articleListState);
	  $stateProvider.state(articleDetailState);
    
});


app.controller('baseCtrl', function($scope, $http, Restangular, readNextService) {
		
	readNextService.get().then(function(articles){
			
			$scope.read_next  = articles;
			_.each(articles, function(ele, index){
				id = "#read-next-" + index;
				$(id).backstretch(ele.hero_image);
			})
		});
	
})