// services module
var app = angular.module("services", []);


// this service will get and handle all the data
// about articles from backend
app.factory('Articles', [ '$http', function($http) {
    // here must be data logic

    function getArticles(chapter) {
        console.log(chapter);
    }

    return {
        getArticles: getArticles
    }

}]);