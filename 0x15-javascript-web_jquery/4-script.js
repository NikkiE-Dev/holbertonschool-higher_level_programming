$("#toggle_header").click( function(e) {
if($("header").hasClass("green")) {
$("header").removeClass("green");
$("header").addClass("red");
} else {
	$("header").removeClass("red");
  $("header").addClass("green");
}
})
