 $(document).ready(function(){
    let autoRefresh = function(){
      $.ajax({
        method:'get',cache: false,
        url:'/ajax/get_feed',
        success:function(data){
          $("#news-feed").html(data);
        }
      });
    }
    setInterval(autoRefresh,20000);
  });