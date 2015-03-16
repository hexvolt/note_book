// controllers module
var app = angular.module("controllers", ['services']);


app.controller('TimelineController', function() {
    this.articles = 'Here will be the articles';

});


app.controller('TabController', [ 'Articles', function(Articles) {
    var tabs = this;

    tabs.activeTab = 1;

    tabs.selectTab = function(tab) {
        // switch the current chapter (tab) and load appropriate content
        tabs.activeTab = tab;
        Articles.getArticles(111);
    };

    tabs.isSelected = function(tab) {
        return tabs.activeTab === tab;
    };
}]);