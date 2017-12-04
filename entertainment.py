import fresh_tomatoes
import media

big_green = media.Movie("Big Green", "Soccer Team who goes from piss poor to Champs",
            "http://www.impawards.com/1995/big_green_xlg.html",
            "https://www.youtube.com/watch?v=C19heV7758U", "1995")

air_force_one=media.Movie("Air Force One", "The President's plane gets taken hostage in air",
              "https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwii1Kzeot_XAhVk1oMKHfZ1DhMQjRwIBw&url=https%3A%2F%2Fwww.clickplay.hk%2Fen-us%2FMovie%2FFilterResult%3Fmode%3Dfilter%26filter_field%3Dgenre%26filter_value%3D%2525%26page_num%3D1%26default_view%3Dposter_view&psig=AOvVaw1BK12ppsEEP-qIUBzNh2y5&ust=1511889846389153",
              "https://www.youtube.com/watch?v=vIHPP7c6GNU", "1997")

elf = media.Movie("Elf", "Elf from the North Pole travels to find his real dad",
      "https://is5-ssl.mzstatic.com/image/thumb/Music6/v4/df/39/40/df394033-be5c-37c5-f354-fd5159ba70d1/UMG_cvrart_00030206652529_01_RGB72_1500x1500_13UMDIM01385.jpg/1200x630bb.jpg",
      "https://www.youtube.com/watch?v=pHTVCq6TDBs", "2003")

forrestgump = media.Movie("Forrest Gump","Chronicle of several decades in the life of slow-witted but good-hearted Alabama man",
               "https://1.bp.blogspot.com/-_fPu93EHH7I/V0vhv2m9ZtI/AAAAAAABG0k/VrMMAeJ9nVE0-dIv8V_icOlcN_bddMN4wCKgB/s400/Forrest-Gump-movie_poster.jpg",
               "https://www.youtube.com/watch?v=bLvqoHBptjg", "1994")

shrek = media.Movie("Shrek", "An ogre's land is taken over by fairy tale characters whom he agrees to help save their land and princess",
                    "https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwii8eCYjd_XAhVH7IMKHc-4AP0QjRwIBw&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FShrek&psig=AOvVaw0gfA1-UXVB06DooeXPWbuM&ust=1511884054170228",
                    "https://www.youtube.com/watch?v=seUURVsRCD4", "2001")

wonder = media.Movie("Wonder", "A boy with a severe facial deformity goes to school",
         "https://www.google.com/imgres?imgurl=http%3A%2F%2Fwww.impawards.com%2F2017%2Fposters%2Fwonder_xlg.jpg&imgrefurl=http%3A%2F%2Fwww.impawards.com%2F2017%2Fwonder_xlg.html&docid=znHaxlfL2e-bkM&tbnid=GT5V4Zhe2jUPtM%3A&vet=10ahUKEwjR0aGIjt_XAhXD44MKHZPpACMQMwg9KAAwAA..i&w=971&h=1500&client=firefox-b-1-ab&bih=821&biw=1045&q=wonder%20poster%20movie&ved=0ahUKEwjR0aGIjt_XAhXD44MKHZPpACMQMwg9KAAwAA&iact=mrc&uact=8",
         "https://www.youtube.com/watch?v=ngiK1gQKgK8", "2017")

movies = [big_green, air_force_one, elf, forrestgump, shrek, wonder] # list created so easy to call the movies in open_movies_pages function

fresh_tomatoes.open_movies_page(movies) #function in fresh_tomatoes that
