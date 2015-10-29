create type temporal as (id integer,nombre text);
select * from 
select * from bee_peticion limit 4 offset 0;
 create or replace function prueva() returns setof temporal as $$
 declare 
  t temporal%rowtype;
 begin
	select id,texto from bee_peticion where id<288 into t;
	
 end;
 $$language plpgsql;

CREATE OR REPLACE FUNCTION new_sof_sol_des(id_des integer,search_ text,order_ integer,start_ integer,length_ integer)
  RETURNS json AS
$BODY$
begin 
	return (SELECT COALESCE(array_to_json(array_agg(row_to_json(p))), '[]') from (
		select s.id,sf.nombre,u.first_name||' '||u.last_name as nom, u.email,case when s.estado = false then
		  'Solicitado' 
		  else
		   'Comfirmado' 
		   end as estado from bee_software as sf 

		 join bee_solicitud as s on (s.software_id=sf.id and sf.desarrollador_id=id_des)
		 join usr_cliente as c on(c.usuario_id=s.cliente_id) 
		 join auth_user as u on(u.id = c.usuario_id)
		 
		left join bee_desarrollos_softwares as ds on (sf.id=sf.id) 
		left join bee_desarrollos as d on(ds.software_id = sf.id) 
		where sf.nombre like '%'||search_||'%' or u.first_name like '%'||search_||'%' or u.last_name like '%'||search_||'%' or u.email  like '%'||search_||'%' order by s.estado limit length_ offset start_
	) p);
end;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION sof_sol_des(integer)
  OWNER TO postgres;

 create or replace function pru(x integer)return 