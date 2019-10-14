togglefollow = (id)=>{
    $.get('/follow_or_not/'+id,(newfollows)=>{
        $("#following").text(newfollows[1]);
        $("#followers").text(newfollows[0]);
        let follow=$("#follow");
        let following=$("#follown");
        if (follow.hasClass("d-none")){
            follow.removeClass("d-none");
            following.addClass("d-none")
        }else{
            following.removeClass("d-none");
            follow.addClass("d-none")
        }
    });
};