// controllers module
var app = angular.module("controllers", ['services']);


app.controller('TimelineController', [ 'Articles', function(Articles) {
    this.articles = Articles.currentArticles;
}]);


app.controller('TabController', [ 'Articles', function(Articles) {
    var tabs = this;

    tabs.activeTab = 1;

    tabs.selectTab = function(tab) {
        // switch the current tab and load appropriate articles
        tabs.activeTab = tab;
        Articles.loadArticles(tab);
    };

    tabs.isSelected = function(tab) {
        return tabs.activeTab === tab;
    };
}]);