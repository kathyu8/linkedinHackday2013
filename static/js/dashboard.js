$(window).load = function() {
	$("#apply").click(applyForm);

	$("#applySelected").click(function(){
		var jobPosts = $("#jobPosts");
		jobPosts.each(function(i, jobPost){
			console.log("clicking on jobPost!");
			if($("willApply:checked").length === 1) {
				applyForm();
			}
			return false;
		});
	});

	$("#applyAll").click(function(){
		var jobPosts = $("#jobPosts");
		jobPosts.each(function(i, jobPost){
			console.log("clicking on jobPost!");
			applyForm();
		});
		return false;
	});
}

function applyForm(){
	console.log("applying!");
	$("#apply").attr("id","applied");
	$("#apply").html("Applied");
	$("#checkmark").show();
	$("#checkmark").attr("display", "inline");
	return false;
}