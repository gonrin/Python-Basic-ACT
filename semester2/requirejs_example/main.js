define(["./mnc", "./startup"], 
   function(mnc, startup) {
        
      return {
         state: "karnataka",
         city: "bangalore",
      
         addCompany: function() {
            mnc.decrement(this);
            startup.add(this);
         }
      
      }
   }
);