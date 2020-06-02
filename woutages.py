import scrapy

class OutageSpider(scrapy.Spider):
    name = 'outagespider'
    campina_grande = 18
    # start_urls = ['http://sic.cagepa.pb.gov.br/sigo_ocorrencia_falta_de_agua_comunicado_suspensao_site_grid/index.php?localidade=campina_grande']
    start_urls = ['http://sic.cagepa.pb.gov.br/sigo_ocorrencia_falta_de_agua_comunicado_suspensao_site_grid/index.php?localidade=18&enviar=OK']

    def parse(self, response):
        for evento in response.css('#sc-ui-grid-body-af2febbe>tr'):
            yield {
                'id': evento.css('td.css_o_codigo_ocorrencia_grid_line ::text').get(),
                'city': evento.css('td.css_c_nome_cidade_grid_line ::text').get(),
                'region': evento.css('td.css_area_afetada_grid_line ::text').get(),
                'begin_time': evento.css('td.css_data_inicio_grid_line ::text').get(),
                'end_time': evento.css('td.css_data_fim_grid_line ::text').get(),
                'reason': evento.css('td.css_motivo_grid_line ::text').get()
            }
