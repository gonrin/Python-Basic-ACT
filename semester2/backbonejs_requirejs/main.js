define('jquery', [], function () {
    return jQuery;
});

define('underscore', [], function () {
    return _;
});

require.config({
    baseUrl: '/baseurl',
    paths: {
        app: '../app_modules'
    },
    shim: {
        'backbone': {
            deps: ['underscore', 'jquery'],
            exports: 'Backbone'
        },
        'underscore': {
            exports: '_'
        }
    },
});

require(['jquery','underscore'], function ($, _){
    console.log("Hello");

});

// define(function (require) {
//     var myteam = require("./team");
//     var mylogger = require("./player");
//     console.log(myteam);
//     alert("Player Name : " + myteam.player);
//     mylogger.myfunc();
//  });