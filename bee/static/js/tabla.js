$(document).ready(function () {
    //tabla();
});
/**
 * Created by mario on 13/08/14.
 */
function tabla(){
    $('.table').dataTable({
        "bPaginate": true,
        "bScrollCollapse": true,
        "sPaginationType": "full_numbers",
        "bRetrieve": true,
         searching: true,
        "oLanguage": {
            "sProcessing": "Procesando...",
            "sLengthMenu": "Mostrar _MENU_ Registros",
            "sZeroRecords": "No se encontraron resultados",
            "sInfo": "Mostrando desde _START_ hasta _END_ de _TOTAL_ Registros",
            "sInfoEmpty": "Mostrando desde 0 hasta 0 de 0 Registros",
            "sInfoFiltered": "(filtrado de _MAX_ registros en total)",
            "sInfoPostFix": "",
            "sSearch": "Buscar:",
            "sUrl": "",
            "oPaginate": {
                "sFirst": "<i>&#xf100;</i>",
                "sPrevious": "<i>&#xf104;</i>",
                "sNext": "<i>&#xf105;</i>",
                "sLast": "<i>&#xf101;</i>"
            }
        }
    });
}

function tabla2(){
    $('.table').dataTable({
        "bPaginate": false,
        "bScrollCollapse": true,
        "sPaginationType": "full_numbers",
        "bRetrieve": true,
         searching: false,
        "oLanguage": {
            "sProcessing": "Procesando...",
            "sLengthMenu": "Mostrar _MENU_ Registros",
            "sZeroRecords": "No se encontraron resultados",
            "sInfo": "Mostrando desde _START_ hasta _END_ de _TOTAL_ Registros",
            "sInfoEmpty": "Mostrando desde 0 hasta 0 de 0 Registros",
            "sInfoFiltered": "(filtrado de _MAX_ registros en total)",
            "sInfoPostFix": "",
            "sSearch": "Buscar:",
            "sUrl": "",
            "oPaginate": {
                "sFirst": "<i>&#xf100;</i>",
                "sPrevious": "<i>&#xf104;</i>",
                "sNext": "<i>&#xf105;</i>",
                "sLast": "<i>&#xf101;</i>"
            }
        }
    });
}