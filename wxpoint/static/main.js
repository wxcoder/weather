$(document).ready(function () {
    $(':button').click(function (){
        var myval = $(this).attr("value");


    $('#post-form').on('submit', function(event) {
        event.preventDefault();
        console.log("form submitted!");
        console.log(myval);
        var cbtn = $("button");
        var btnval = cbtn.val();
        console.log(cbtn);
        document.getElementById('gbimg').style.display = 'none';
        document.getElementById('rgimg').style.display = 'none';
        create_post(myval);
        
    });
});


    function create_post(btnval) {
        console.log("create post is working!");
        $.ajax({
           url : "create_post/",
            cache : 'false',
            type : "POST",
            data : { initmdls : btnval},

            success : function(json) {
                console.log(json.result);
                var check=document.getElementById('modelerror');
                if(check) {
                    check.parentNode.removeChild(check);
                }
                $("#modelimages").prepend("<img src="+json.result+" class='img-responsive thumbnail'>");
            },

            error : function(xhr,errmsg,err) {
                $('#modelimages').prepend("<p id='modelerror'>Image Does Not Exist<p>")
            }


        });    
    };
});


// This function gets cookie with a given name
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');
 
/*
The functions below will create a header with csrftoken
*/
 
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
function sameOrigin(url) {
    // test that a given url is a same-origin URL
    // url could be relative or scheme relative or absolute
    var host = document.location.host; // host + port
    var protocol = document.location.protocol;
    var sr_origin = '//' + host;
    var origin = protocol + sr_origin;
    // Allow absolute or scheme relative URLs to same origin
    return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
        (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
        // or any other URL that isn't scheme relative or absolute i.e relative.
        !(/^(\/\/|http:|https:).*/.test(url));
}
 
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
            // Send the token to same-origin, relative URLs only.
            // Send the token only if the method warrants CSRF protection
            // Using the CSRFToken value acquired earlier
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
