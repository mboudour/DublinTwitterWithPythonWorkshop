require 'fileutils'
# gem install capybara
# gem install pry
# gem install selenium-webdriver
# gem install chromedriver-helper
# gem install twitter
# script_dir='/Users/mosesboudourides/GithubRepositories/TwitterMining/'
# script_dir='/home/sergios-len/Documents/githubs/TwitterMining/'
# script_dir='/home/mab/github_repos/TwitterMining/'
# whereiam= Dir.pwd
# Dir.chdir script_dir
# print Dir.pwd
require_relative 'twitter_scrap'
out_dir='scraping_tweet'
# out_dir='/home/sergios-len/Documents/githubs/TwitterMining/Output'
# out_dir='/home/mab/Desktop/twitTemp/Output'
Dir.chdir out_dir

with_time_zone  'UTC' do #'America/New_York'
  # searchterm='EUSN' #hashtag=true
  # searchterm='day%20night%20paris' #hashtag=false
  searchterm='aylankurdi' #hashtag=false
  from='2015-09-01'
  pages = 100 #500 You have to figure out what is yours browser capabilities
  cccc = 50
  to = '2015-10-31'
  check = nil
  begin
    t_search=SearchTwitter.new(searchterm,from,to,hashtag=false) # hashtag = false returns both # and non #
    t_search.scrap_twitter_page(pages,cccc)
    new_to=t_search.get_date

    new_to = t_search.get_date
  #     p check,new_to, 'check first'
    if check == new_to
        t_search.write_html
        t_search.close_search
        puts 'Done'
        break
    end


    new_to_day = new_to.prev_day.day
    puts new_to.hour
    if  Date.new(new_to.year,new_to.mon,new_to.mday).to_s <= from
        t_search.write_html
        t_search.close_search
        puts 'Finish searching'
        break

    elsif new_to.hour < 8 
        npages = pages
        begin
            t_search.scrap_twitter_page(cccc * 2 , 25,npages)
            new_to = t_search.get_date
            if check == nil 
                check= new_to
            elsif check > new_to
                check = new_to
            elsif check == new_to
                puts 'I m out'
                break   
            end
            npages += cccc*2
        end until (new_to.day <=> new_to_day) == -1 
    end
    puts 'Still scraping'
    nto= new_to.next
    to = Date.new(nto.year,nto.mon,nto.mday).to_s
    tot = Date.new(new_to.year,new_to.mon,new_to.mday).to_s
  #   puts to,tot
    t_search.write_html
    t_search.close_search
  end until from == tot 
end