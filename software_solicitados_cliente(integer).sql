-- Function: software_solicitados_cliente(integer)

-- DROP FUNCTION software_solicitados_cliente(integer);

CREATE OR REPLACE FUNCTION software_solicitados_cliente(id_cli integer)
  RETURNS json AS
$BODY$
begin
	return (SELECT COALESCE(array_to_json(array_agg(row_to_json(p))), '[]') from (
		select distinct on(sof.id) sof.id as pk ,regexp_replace(sof.descripcion,'(\n|\r|\t)+','<br>') as descripcion,sof.imagen,sof.nombre,
		case when s.estado = null then
		 'Solicitar'
		 when s.estado = false then
		  'Solicitado' 
		  else
		   'Asignado' 
		   end from bee_solicitud as s 
			inner join bee_software as sof on (s.software_id=sof.id and s.cliente_id=id_cli) order by sof.id
	) p);
end;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION software_solicitados_cliente(integer)
  OWNER TO postgres;
