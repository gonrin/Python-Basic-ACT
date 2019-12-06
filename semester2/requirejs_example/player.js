define(function (require) {
    var myteam = require("./team");
 
    return {
       myfunc: function () {
          document.write("Name: " + myteam.player + ", Country: " + myteam.team);
       }
    };
 });