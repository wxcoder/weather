
$(document).ready(function () {
/*
    $('#post-form').on('submit', function(event) {
            event.preventDefault();
            var val = $("button[type=submit][clicked=true]").val();
            document.getElementById('gbimg').style.display = 'none';
            document.getElementById('rgimg').style.display = 'none';
            create_post(val);
        
    });

    $("#post-form button[type=submit]").click(function() {
        $("button[type=submit]", $(this).parents("#post-form")).removeAttr("clicked");
        $(this).attr("clicked", "true");
    });
*/ 
    //form to process model based on button value
    $('#post-form').on('submit', function(event) {
        event.preventDefault();
    });
//    $('#post-form button').click(function (){
/*
    $('button[name=models]').click(function (){
        var myval = $(this).attr("value");
        document.getElementById('gbimg').style.display = 'none';
        document.getElementById('rgimg').style.display = 'none';
        create_post(myval);
        var check = document.getElementsByName("models");
        for(var z = 0; z < check.length; z++){
            if(check[z].disabled) {
                check[z].disabled=false;
            }
        }
        $(this).attr("disabled","true");


    });
    //Load initial model image
   function create_post(btnval) {
        $.ajax({
           url : "create_post/",
            cache : 'false',
            type : "POST",
            data : { initmdls : btnval},

            success : function(json) {
                var mcheck=document.getElementById('mimage');
                if(!mcheck) {
                    $("#modelimages").prepend("<img src="+json.result+" class='img-responsive thumbnail' id='mimage'>");
                } else {
                    mcheck.src=json.result;
                }


            },

            error : function(xhr,errmsg,err) {
                var mcheck=document.getElementById('mimage');
                if(mcheck) {
                    mcheck.parentNode.removeChild(mcheck);
                }
            }


        });

        var checkbuttons = document.getElementById('allbuttons');
        console.log(checkbuttons);
        if(checkbuttons) {
            checkbuttons.parentNode.removeChild(checkbuttons);
            create_buttons(btnval);
        } else {
            create_buttons(btnval);
        }    
    };


    function create_buttons(btnval) {
        var modeldiv = document.getElementById('allbuttons');
        var num_buttons = {'GFS':[384,6,14,0], 'ECMWF':[240,24,3,2],'CMC':[240,6,11,0],'NAM':[84,3,8,0],'RGEM':[48,3,5,0]};
        var tbl=document.createElement('table');
        tbl.style.width='20%';
        tbl.style.height = "30%"
        tbl.id="allbuttons";
        var tbdy=document.createElement('tbody');
        //if(btnval == 'GFS') {
        var buttonval = [];
        for(var a=0; a <= num_buttons[btnval][0]; a+=num_buttons[btnval][1] ) {
            if(a <= 240) {
                buttonval.push(a.toString());
            } else {
                a +=6;
                buttonval.push(a.toString());
            }
        }
        for(var i = 0; i < num_buttons[btnval][2]; i++) {
            var tr= tbl.insertRow();
            for(var j = 0; j < 4; j++ ) {
                if( i == (num_buttons[btnval][2] - 1) && j > num_buttons[btnval][3]) {
                    break;
                
            } else {
                var td = tr.insertCell();
                var btn = document.createElement("button");
                btn.className= "btn btn-default";
                btn.name = btnval;
                btn.value=(buttonval[0])
                var t = document.createTextNode(buttonval[0]);
                buttonval.shift();
                btn.appendChild(t);
                td.appendChild(btn);

                }
            }
        }   
        $('#mbutton-form').prepend(tbl);
    };

    $("#mbutton-form").on('submit', function(event) {
        event.preventDefault();
    });

    $('#mbutton-form button').click(function() {
        var mname = $(this).attr("name");
        var mhr = $(this).attr("name");

    });

*/
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
});
