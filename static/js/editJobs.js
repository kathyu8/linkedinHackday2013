$(document).ready(function() {  
  
 $("#university").bind("keyup", function () {  
  
  /* replaces text as you type with hashtags */  
  
  var input = $(this);  
  var value = input.val();  
  var ends_with_space = (value.substr(-1) == " ");  
  
  var hashed_value = "";  
  var parts = value.split(" ");  
  for (var i = 0; i < parts.length; i++) {  
   var part = parts[i];  
   if (part.indexOf("#") != 0) {  
    part = "#" + part;  
   }  
   if (part != "#") {  
    if (hashed_value == "") {  
     hashed_value = part;  
    } else {  
     hashed_value += " " + part;  
    }  
   }  
  }  
  if (ends_with_space) {  
   hashed_value = hashed_value + " ";  
  }  
  input.val(hashed_value.replace(",", ""));  
 });  
  
});  