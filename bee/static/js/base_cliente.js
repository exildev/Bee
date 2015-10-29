/**
 * Created by dreicon88 on 15/02/15.
 */

$(document).on('ready',function(){
    $('.stop').on('click',function(){
        return false;
    });
    $('.busqueda').on('click',function(){
    	$('#buscar').load($(this).find('a').attr('href'));
    });
    $('.medida').on('click',function(){
        $('#buscar').load($(this).find('a').attr('href'),function(){
            cargarContenido();
        });
    });
    $('.contacto').on('click',function(){
        $('#buscar').load($(this).find('a').attr('href'),function(){
            cargarContenido();
        });
    });
    $("#buscar form").ajaxForm({
        beforeSubmit:function(){
            cargando();
        },
        success: function (data) {
            cargando();
            $("#buscar").html(data);
        },
        error: function () {
            cargando();
            alert("Problemas con laconexion");
        }
    });
});

function cargarContenido(){
    $("#form").ajaxForm({
        target: '#buscar'
    });
    $('textarea').prop('required',true);
}
