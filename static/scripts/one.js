$(document).ready( function() {

    $(".yolo").click(function(){
        $.ajax({url: "/jportal/job_approval/", success: function(result){
            html_content = "<button>" + result + "</button>";
            $(".st").html(html);
        }, 
        type: "GET"
        });
    });

});
