-- Function: get_solicitudes(integer)

-- DROP FUNCTION get_solicitudes(integer);

CREATE OR REPLACE FUNCTION get_solicitudes(id_des integer)
  RETURNS json AS
$BODY$
begin
	return (SELECT COALESCE(array_to_json(array_agg(row_to_json(p))), '[]') from (
		select s.id as id,u.first_name||' '||u.last_name as nombre,u.email,s.descripcion as des,s.estado as estado from  bee_sofwarerequerido as s 
		inner join auth_user as u on(u.id=s.cliente_id) where s.estado=false or s.desarrollador_id=id_des
	) p); 		
end;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION get_solicitudes(integer)
  OWNER TO postgres;
