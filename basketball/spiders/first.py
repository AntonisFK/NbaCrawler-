import scrapy 


class FirstSpider(scrapy.Spider):
  name = "first"
  allowed_domains = ["www.basketball-reference.com/"]
  start_urls = [
  'http://www.basketball-reference.com/players/c/curryst01.html'
  ]


  def parse(self, response):

    table_row = response.xapth('//*[@id="per_game"]/thead/tr')

    Item['title'] = response.xpath('//*[@id="all_per_game"]/div[1]/h2/text()').extract()[0]
    Item['player'] = response.xpath('//*[@id="info_box"]/h1/text()').extract()[0]

    for rows in table_row:


      Item['Season'] = rows.response.xpath('//*[@id="per_minute.2013"]/td//text()').extract()[0]
      Item['Age'] = rows.response.xpath('//*[@id="per_minute.2013"]/td//text()').extract()[1]
      Item['Tm'] = rows.response.xpath('//*[@id="per_minute.2013"]/td//text()').extract()[2]
      Item['Lg'] = rows.response.xpath('//*[@id="per_minute.2013"]/td//text()').extract()[3]
      Item['Pos'] = rows.response.xpath('//*[@id="per_minute.2013"]/td//text()').extract()[4]
      Item['G'] = rows.response.xpath('//*[@id="per_minute.2013"]/td//text()').extract()[5]
      Item['GS'] = rows.response.xpath('//*[@id="per_minute.2013"]/td//text()').extract()[6]
      Item['MP'] = rows.response.xpath('//*[@id="per_minute.2013"]/td//text()').extract()[7]
      Item['FG'] = rows.response.xpath('//*[@id="per_minute.2013"]/td//text()').extract()[8]
      Item['FGA'] = rows.response.xpath('//*[@id="per_minute.2013"]/td//text()').extract()[9]
      Item['FGP'] = rows.response.xpath('//*[@id="per_minute.2013"]/td//text()').extract()[10]
      Item['ThreeP'] = rows.response.xpath('//*[@id="per_minute.2013"]/td//text()').extract()[11]
      Item['ThreePA'] = rows.response.xpath('//*[@id="per_minute.2013"]/td//text()').extract()[12]
      Item['Threepp'] = rows.response.xpath('//*[@id="per_minute.2013"]/td//text()').extract()[13]
      Item['TwoP'] = rows.response.xpath('//*[@id="per_minute.2013"]/td//text()').extract()[14]
      Item['TWOPA'] = rows.response.xpath('//*[@id="per_minute.2013"]/td//text()').extract()[15]
      Item['TWOP'] = rows.response.xpath('//*[@id="per_minute.2013"]/td//text()').extract()[16]
      Item['FT'] = rows.response.xpath('//*[@id="per_minute.2013"]/td//text()').extract()[17]
      Item['FTA'] = rows.response.xpath('//*[@id="per_minute.2013"]/td//text()').extract()[18]
      Item['FTP'] = rows.response.xpath('//*[@id="per_minute.2013"]/td//text()').extract()[19]
      Item['ORB'] = rows.response.xpath('//*[@id="per_minute.2013"]/td//text()').extract()[20]
      Item['DRB'] = rows.response.xpath('//*[@id="per_minute.2013"]/td//text()').extract()[21]
      Item['TRB'] = rows.response.xpath('//*[@id="per_minute.2013"]/td//text()').extract()[22]
      Item['AST'] = rows.response.xpath('//*[@id="per_minute.2013"]/td//text()').extract()[23]
      Item['BLK'] = rows.response.xpath('//*[@id="per_minute.2013"]/td//text()').extract()[24]
      Item['TOV'] = rows.response.xpath('//*[@id="per_minute.2013"]/td//text()').extract()[25]
      Item['PF'] = rows.response.xpath('//*[@id="per_minute.2013"]/td//text()').extract()[26]
      Item['PTS'] = rows.response.xpath('//*[@id="per_minute.2013"]/td//text()').extract()[27]

      yield item

      #table name = response.xpath('//*/div/h2/text()').extract()
      #title row = response.xapth('//*[@id="per_game"]/thead/tr')        
      #title  = response.xpath('//*[@id="per_minute"]/thead/tr/th/text()').extract()
      #row = response.xpath('//*[@id="per_game"]/tbody//tr')
      #data =response.xpath('//*[@id="per_minute.2013"]/td//text()').extract()
      #carrer = response.xpath('//*[@id="per_minute"]/tfoot/tr/td/text()').extract()
