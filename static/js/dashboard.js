$(document).ready(function() {  

	$("#saveBtn").on("click", function() {
		console.log("clicked");
		$("#saveBtn").css("opacity", 1);
	});

	$("#apply").click(applyForm);

	$("#applySelected").click(function(){
		var jobPosts = $(".jobPost");
		jobPosts.each(function(i, jobPost){
			console.log("clicking on jobPost!");
			if($("willApply:checked").length === 1) {
				applyForm();
			}
			return false;
		});
	});

	$("#applyAll").click(function(){
		var jobPosts = $(".jobPost");
		jobPosts.each(function(i, jobPost){
			console.log("clicking on jobPost!");
			applyForm();
		});
		return false;
	});

    function applyForm(){
    	console.log("applying!");
    	$("#apply").html("Applied");
        $("#apply").attr("id","applied");
    	$("#checkmark").css("display", "inline-block");
    	return false;
    }

    $('#university').click(function() {
        var $this = $(this);
        if ($this.is(':checked')) {
            var filter = $("#uni-options :selected").text();
            $('.job-uni').each(function(i, obj) {
                 if ($(this).html().indexOf(filter) == -1) {
                    $(this).parents(".jobPost").hide();
                 }
            });
        } else {
            $('.job-uni').each(function(i, obj) {
                $(this).parents(".jobPost").show();
            });
        }
    });

    $('#uni-options').change(function() {
        var filter = $("#uni-options :selected").text();
        $('.job-uni').each(function(i, obj) {
             if ($(this).html().indexOf(filter) == -1) {
                $(this).parents(".jobPost").hide();
             } else {
                $(this).parents(".jobPost").show();
             }
        });
    });

});

