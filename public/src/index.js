// Angularjs require
var angular = require('angular');
require('angular-route');
require('ng-file-upload');
require('angular-sanitize');


// AngularJS module working
var app = angular.module('App', ['ngRoute', 'ngFileUpload', 'ngSanitize']);
app.config(function($routeProvider) {
    $routeProvider.when('/', {
        controller: 'Email',
        templateUrl: '/email.html'
    })
    .when('/event', {
        controller: 'Event',
        templateUrl: '/event.html'
    })
    .when('/send_emails', {
        controller: 'SendEmails',
        templateUrl: '/send_emails.html'
    });
});

// Factories
app.factory('Http', require('./http'));

// Controllers
app.controller('Email', require('./controllers/email'));
app.controller('Event', require('./controllers/event'));
app.controller('SendEmails', require('./controllers/send_emails'));