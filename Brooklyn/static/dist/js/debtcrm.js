//$(document).ready(function() {
  //$(function () {
    //$('.example1').DataTable()
    //$('#example2').DataTable({
    //  'paging'      : true,
    // 'lengthChange': false,
    //  'searching'   : false,
    //  'ordering'    : true,
    //  'info'        : true,
    //  'autoWidth'   : false
    //})
  //})

  function search() {
    tr = $("#id_name").val();
    alert(tr);
    
    $.ajax(
      {
          type:"GET",
          url: "/search",
          data:{
               name: tr
          },
          dataType: 'json',
          success: function(data)
          {
            
              console.log(data)
          }
      })

  }
//}