$('#status_btn').click(function(){

var order_id = $('#status_btn').attr('data-id')
var status = $('#status_btn').text()

if (status == 'pending'):{
    var url = '/orders/pending/'
    var btn_text = 'confirmed'
    var btn_class = 'btn btn-success'
}else{
    var url = '/orders/confirmed/'
    var btn_text = 'pending'
    var btn_class = 'btn btn-warning'
}

    $.ajax({
        url: url,
        method: 'POST',
        data:{
            'order_id': order_id,
        },
        success: function(data){
            if(data['status'] == 'ok'){
                $('#status_btn').text(btn_text)
                $('#status_btn').attr({'class': btn_class})
            }
        }

    });

});