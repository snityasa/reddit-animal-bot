import praw

reddit = praw.Reddit(
    client_id="****************",
    client_secret="****************",
    user_agent="<console:ENDANGERED:1.0>"
)

subreddit = reddit.subreddit("AnimalsBeingBros")

animal_descriptions = ["African forest elephants are the elusive cousin of the African savanna elephant. They inhabit the dense rainforests of west and central Africa.  They are smaller than African savanna elephants, the other African elephant species. Their ears are more oval-shaped and their tusks are straighter and point downward (the tusks of savanna elephants curve outwards). ",
                       "People usually think of leopards in the savannas of Africa but in the Russian Far East, a rare subspecies has adapted to life in the temperate forests that make up the northern-most part of the species’ range. Similar to other leopards, the Amur leopard can run at speeds of up to 37 miles per hour. This incredible animal has been reported to leap more than 19 feet horizontally and up to 10 feet vertically.",
                       "Black rhinos are the smaller of the two African rhino species. The most notable difference between white and black rhinos are their hooked upper lip. This distinguishes them from the white rhino, which has a square lip. Black rhinos are browsers rather than grazers, and their pointed lip helps them feed on leaves from bushes and trees. They have two horns, and occasionally a third, small posterior horn.",
                       "Scientists have been unable to thoroughly study the distribution and abundance of the Cross River gorilla until the last decade or so. Because the gorillas are wary of humans and inhabit rugged territory, scientists have been unable to count many of these gorillas directly. Instead, researchers have used indirect signs, such as nest counts, and estimated range sizes to determine that there are only about 200 to 300 of these gorillas left in the wild. Cross River gorillas are scattered in at least 11 groups across the lowland montane forests and rainforests of Cameroon and Nigeria, an area of 3,000 square miles, or about twice the size of Rhode Island.",
                       "The eastern lowland gorilla—also known as Grauer’s gorilla—is the largest of the four gorilla subspecies. It is distinguished from other gorillas by its stocky body, large hands and short muzzle. Despite its size, eastern lowland gorillas subsist mainly on fruit and other herbaceous materials, just like other gorilla subspecies.",
                       "Hawksbills are named for their narrow, pointed beak. They also have a distinctive pattern of overlapping scales on their shells that form a serrated-look on the edges. These colored and patterned shells make them highly-valuable and commonly sold as 'tortoiseshell' in markets.",
                       "Javan rhinos are the most threatened of the five rhino species, with only around 60 individuals that live only in Ujung Kulon National Park in Java, Indonesia. Javan rhinos once lived throughout northeast India and Southeast Asia. Vietnam’s last Javan rhino was poached in 2010.",
                       "The name orangutan means 'man of the forest' in the Malay language. In the lowland forests in which they reside, orangutans live solitary existences. They feast on wild fruits like lychees, mangosteens, and figs, and slurp water from holes in trees. They make nests in trees of vegetation to sleep at night and rest during the day.",
                       "The saola was discovered in May 1992 during a joint survey carried out by the Ministry of Forestry of Vietnam and WWF in north-central Vietnam. The team found a skull with unusual long, straight horns in a hunter's home and knew it was something extraordinary. The find proved to be the first large mammal new to science in more than 50 years and one of the most spectacular zoological discoveries of the 20th century.",
                       "Sumatran elephants feed on a variety of plants and deposit seeds wherever they go, contributing to a healthy forest ecosystem. They also share their lush forest habitat with several other endangered species, such as the Sumatran rhino, tiger, and orangutan, and countless other species that all benefit from an elephant population that thrives in a healthy habitat.",
                       "Sumatran rhinos are the smallest of the living rhinoceroses and the only Asian rhino with two horns. They are covered with long hair and are more closely related to the extinct woolly rhinos than any of the other rhino species alive today. Calves are born with a dense covering that turns reddish-brown in young adults and becomes sparse, bristly and almost black in older animals. Sumatran rhinos compete with the Javan rhino for the unenviable title of most threatened rhino species. While surviving in possibly greater numbers than the Javan rhino, Sumatran rhinos are more threatened due to habitat loss and fragmentation. The remaining animals survive in small, fragmented non-viable populations, and with limited possibilities to find each other to breed, its population decline continues. Just two captive females have reproduced in the last 15 years.",
                       "This subspecies was once found across several parts of the Sunda islands in Indonesia. Today, all remaining Sunda tigers are found only in Sumatra, now that tigers in Java and Bali are extinct. Sunda tigers are distinguished by heavy black stripes on their orange coats. ",
                       "Vaquita, the world's rarest marine mammal, is on the edge of extinction. The plight of cetaceans—whales, dolphins, and porpoises—as a whole is exemplified by the rapid decline of the vaquita in Mexico, with about 10 individuals remaining. This little porpoise wasn't discovered until 1958 and a little over half a century later, we are on the brink of losing them forever. Vaquita are often caught and drowned in gillnets used by illegal fishing operations in marine protected areas within Mexico's Gulf of California. The population has dropped drastically in the last few years.",
                       "The western lowland gorilla is the most numerous and widespread of all gorilla subspecies. Populations can be found in Cameroon, the Central African Republic, the Democratic Republic of Congo and Equatorial Guinea as well as in large areas in Gabon and the Republic of Congo. The exact number of western lowland gorillas is not known because they inhabit some of the most dense and remote rainforests in Africa. ",
                       "The Yangtze River, the longest river in Asia, used to be one of the only two rivers in the world that was home to two different species of dolphin—the Yangtze finless porpoise and the Baiji dolphin. However, in 2006 the Baiji dolphin was declared functionally extinct. This was the first time in history that an entire species of dolphin had been wiped off the planet because of human activity. Its close cousin, the Yangtze finless porpoise, is known for its mischievous smile and has a level of intelligence comparable to that of a gorilla."] 

for submission in subreddit.hot(limit=5):
    for comment in submission.comments:
        if hasattr(comment, "body"):
            lowcase_comment = comment.body.lower()
            if " african forest elephant " in lowcase_comment:
                comment.reply(animal_descriptions[0])
            if " amur leopard " in lowcase_comment:
                comment.reply(animal_descriptions[1])
            if " black rhino " in lowcase_comment:
                comment.reply(animal_descriptions[2])
            if " cross river gorilla " in lowcase_comment:
                comment.reply(animal_descriptions[3])
            if " eastern lowland gorilla " in lowcase_comment:
                comment.reply(animal_descriptions[4])
            if " hawksbill turtle " in lowcase_comment:
                comment.reply(animal_descriptions[5])
            if " javan rhino " in lowcase_comment:
                comment.reply(animal_descriptions[6])
            if " orangutan " in lowcase_comment:
                comment.reply(animal_descriptions[7])
            if " saola " in lowcase_comment:
                comment.reply(animal_descriptions[8])
            if " sumatran elephant " in lowcase_comment:
                comment.reply(animal_descriptions[9])
            if " sumatran rhino " in lowcase_comment:
                comment.reply(animal_descriptions[10])
            if " sunda tiger " in lowcase_comment:
                comment.reply(animal_descriptions[11])
            if " vaquita " in lowcase_comment:
                comment.reply(animal_descriptions[12])
            if " western lowland gorilla " in lowcase_comment:
                comment.reply(animal_descriptions[13])
            if " yangtze finless porpoise " in lowcase_comment:
                comment.reply(animal_descriptions[14])
                