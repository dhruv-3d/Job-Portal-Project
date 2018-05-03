$(document).ready( function() {

    $(".action").click(function() {
        var seeker_id;
        seeker_id = $(this).attr("id");
        job_id = $(this).attr("value");
        getAction(seeker_id, job_id);
    });

    function getAction(seeker_id, job_id) {
        $(".approve").click(function() {
            var ap_action;
            ap_action = $(this).attr("value");

            $.ajax({url: "/jportal/job_approval/",
                data: { status: ap_action, seeker: seeker_id, job: job_id },
                success: function(result){
                    $(document).find('#' + 'applicant_' + seeker_id).text('Approved');
                    console.log("Server response", JSON.parse(result));
                }
            });
        });

        $(".reject").click(function() {
            var ap_action;
            ap_action = $(this).attr("value");

            $.ajax({url: "/jportal/job_approval/",
                data: { status: ap_action, seeker: seeker_id, job: job_id },
                success: function(result){
                    $(document).find('#' + 'applicant_' + seeker_id).text('Rejected');
                    console.log("Server response", JSON.parse(result));
                }
            });
        });
    }
    

});