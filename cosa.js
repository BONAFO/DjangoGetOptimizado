let query = window.location.href.replace(window.origin, "1|");
 query = window.location.href.replace(window.location.pathname, "1|");



 if(query.includes("?")){
    query = "?p=t";
 }else{
    query = "&p=t";
 }  