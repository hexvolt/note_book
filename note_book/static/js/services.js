// services module
var app = angular.module("services", []);


// this service will get and handle all the data
// about articles from backend
app.factory('Articles', [ '$http', function($http) {
    // the data logic only
    var currentArticles = [
        { title: "Asss sss" },
        { title: "Bsss sss" }
    ];

    function loadArticles(chapter) {
        // updates the list of current articles accordingly to filter params
        var queryParams = {
            params: {
                chapter: chapter
            }
        };
        // get the list of appropriate articles from backend
        $http.get('/articles/', queryParams).success(function(data) {
            // exchanging
            currentArticles.length = 0;
            $.each(data.articles, function( index, article ) {
                currentArticles.push(article);
            });
        });
    }

    return {
        currentArticles: currentArticles,
        loadArticles: loadArticles
    }

}]);