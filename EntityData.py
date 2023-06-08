text = """
permit_product_level → permit_product_level_name, mfg_id, eff_date, end_date, permit_product_level_id

permit_purchase_unit → permit_purchase_unit_name, mfg_id, eff_date, end_date

"""

extra_text = """
sku_type → sku_type_id, sku_type, sku_type_desc, bundle_flag, manual_flag, comp_maint_flag, nexus_safe_flag, include_in_mart_flag, show_cost_form_flag, autogen_new_sku_flag, update_dts, update_uid, inventory_flag, leadtime_flag
product_flag_type → product_flag_type_id, product_flag_type
"""

boiler_code = """
package com.comp.project.cache.entity;

import java.sql.Timestamp;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;

@Entity
@Table(name = "{0}")
public class {1} """

column_boiler_code = """
	@Column(name="{}")
	private {} {};
"""

id_boiler_code = """
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	@Column(name="{}")
	private Integer {};
"""

repo_boiler_code = """package com.comp.project.cache.dao;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.comp.project.cache.entity.{};


@Repository
public interface {}Repository extends JpaRepository<{}, Integer> """

service_bolier_code = """
	public void load{0}Repository() {{
		try {{
			List<{1}> {2}s = {3}Repository.findAll();
			redisTemplate.delete("{4}");
			Gson gson = new Gson();
			{5}s.parallelStream().forEach({6}->{{
				String json = gson.toJson({7});
				redisTemplate.opsForHash().put("{8}", 
						String.valueOf({9}.get{10}Id()), json);
			}});			
		}}
		catch (Exception e) {{
			logger.error("Error in load{11}Repository {{}}",e.getMessage());
		}}
	}}
"""

autboiler_code = """
	@Autowired
	{0} {1};

"""

load_boiler_code = """load{0}Repository();
"""

junit_boiler_code = """
package com.comp.team.project.catalog.handler.entity;

import static org.junit.jupiter.api.Assertions.assertNull;

import org.junit.jupiter.api.Test;

class {0}Test {{

	private {0} {1};
	

	@Test
	void test() {{
		{1} = new {0}();
		
{2}
	}}

}}

"""

setter_boiler_code = """{0}.{1}(null);"""

getter_boiler_code = """assertNull({0}.{1});"""


test_mock_boiler_code = """
@Mock
List<{0}> {1};
"""

test_when_boiler_code = """when({0}).thenReturn({1});
"""

test_new_object = """
        {0} = new ArrayList<{1}>() {{{{
                    add(new {1}());
                }}}};
"""

redis_boiler_delete = """when(redisTemplate.delete("{0}")).thenReturn(null);
"""

test_function_boiler_code = """
	@Test
	@SuppressWarnings("serial")
	void {0}Test() {{
        {1}

		{2}
		{3}
		teamCacheService.{0}();
		{4}thenReturn(null);
		teamCacheService.{0}();
		assertNull(null);
	}}
"""

constructor_boiler_code = """doNothing().when(new teamCacheService()).{0};
"""

meth_code = """
		
"""


sql_boiler_code = """exec sp_help {0}
"""
