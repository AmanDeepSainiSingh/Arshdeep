import streamlit as st
import time

# Set up session state for tracking progress
if 'current_step' not in st.session_state:
    st.session_state.current_step = 1  # Start with the authentication page

# Set up session state to control button visibility
if 'started_treasure_hunt' not in st.session_state:
    st.session_state.started_treasure_hunt = False

# Function to move to the next step
def proceed_to_next_step(step):
    st.session_state.current_step = step

# 1. Authentication Page
def authenticator():
    st.title("🔒 Welcome to Your Birthday Treasure Hunt, Arsh! 🎉")
    st.header("This Quest is Exclusively for You! 🌟")
    st.markdown("""
        #### 🎂 Hello, Birthday Girl! 🎂  
        Today is all about YOU and the incredible journey we've shared. This treasure hunt is designed to celebrate our special bond, filled with fun games, riddles, and surprises. But first, we need to make sure it’s really YOU! 💁‍♀️

        Think of this as a VIP entrance to your birthday adventure! Only those who know your secret access code can enter. And, spoiler alert: that's just YOU. 😉  

        🕵️‍♀️ **Why the check?** Well, we wouldn’t want anyone else sneaking in and taking a peek at all the memories, would we? So, let’s get you verified and into the fun part! 🌈🔒

        Enter your **email** and **password** below, and let’s kick off this exciting journey!  
    """)

    # Email and password input fields
    email = st.text_input("📧 Email")
    password = st.text_input("🔑 Password", type="password")

    if st.button("Authenticate"):
        # Authentication check
        if email.lower() == "ahkaur77@gmail.com" and password == "Arsh2004":
            st.success("✅ Authentication Successful! Welcome, Arsh! 🎈 Let’s start the adventure!")
            # Show confetti effect
            st.snow()
            st.button("Proceed to the Next Section", on_click=proceed_to_next_step, args=(2,))
        else:
            st.error("🚫 Incorrect email or password. Please try again!")

    # Important note below the button
    st.markdown("""
        ---
        ⚠️ **Important Note**: Please don’t refresh the page, or you’ll have to start all over again! 🌀  
        We wouldn’t want that to happen, would we? So keep calm and keep going! 🚀
    """)


# 2. Introduction Page
def introduction():
    st.title("🎉 Happy 20th Birthday, Arsh! 🎉")
    st.markdown("""
        #### 🌟✨ Dearest Cousin-Sister, a Very Happy Birthday to You! ✨🌟

        🎉🎂 **Wow, what a journey we have had together!** It's incredible to think that until May 2023, I had no idea you even existed in my life. But fate had other plans, and our paths crossed at Gopi Paji's wedding in Surrey, Vancouver. Indian weddings are a whirlwind of activity, and amidst all the chaos, I couldn't find the right moment to talk to you. 😅

        🌸 **However, destiny had a better plan in store for us**—when we met again in Woodstock after the wedding, I realized just how amazing you are. 🌸 From that day forward, you have filled my life with love, laughter, and endless memories.

        💖 **You, my dear cousin, have a soul that shines brighter than the stars.** You’ve taught me the true essence of family, how cousins can be a lifeline even when miles apart. You've taken up a permanent residence in my heart, and I wouldn't have it any other way. 💖

        🤣 **And oh, the pranks!** Our daily conversations have become a treasure trove of jokes, deep discussions, shared experiences, and our unique song suggestions. We’ve laughed, we’ve cried, and we’ve bonded in ways that only true soulmates can.

        📅 **Remember these dates?** We met on (02/05/2023), and when I mustered the courage to ask for your number at the Casino in Niagara Falls (12/05/2023). From then on, it has been a journey filled with countless heart-to-heart moments. 📅

        💬 **But the most magical part is that you're the one person who knows everything about me.** Our bond is beyond words, and I hope it lasts until the end of time. This book I’ve written for you is a testament to that bond—a story of how we became more than just cousins, but the best of friends for life. 📝

        🎈 **And today, on this special day**, let's celebrate not just a birthday but the journey of our friendship—the bond that has grown deeper with each passing day. 🎈

        🌟 **From the depths of my heart**, I wish you a world full of happiness, love, and success. And as we step into this new year of your life, I hope this treasure hunt brings you as much joy as you’ve brought into my life! 🌟

        🎁 **But wait! Before you can receive your ultimate gift—the book that captures our journey—you'll need to prove yourself worthy by solving a series of games and challenges. Are you ready?** 🎁

        🥳 Click the button below to start your adventure, and let the balloons fly high in celebration! 🎈🎈
    """)

    if st.button("Start the Treasure Hunt"):
        # Show balloons for celebration
        st.balloons()
        st.session_state.started_treasure_hunt = True  # Update the session state to indicate the treasure hunt has started
        time.sleep(2)  # Pause to let the balloons finish

    # Conditionally display the "Proceed to the Scrabble Game" button only after the treasure hunt has started
    if st.session_state.started_treasure_hunt:
        st.button("Proceed to the Scrabble Game", on_click=proceed_to_next_step, args=(3,))

# 3. Scrabble Game Section
def scrabble_game():
    st.title("🧩 Scrabble Game: Unscramble the Words!")
    st.markdown("""
        #### 🥳 Let's Warm Up with Some Fun Scrabble Words! 🎉  
        
        Before we dive into the more challenging parts of this treasure hunt, let's start with something light and fun—a **Scrabble Game**! 🎲 We're going to test your skills with a series of scrambled words that hold special meaning between us. Each word is like a little piece of our shared story. 📝💕

        🤔 **How does it work?**  
        I've mixed up some words that are tied to our memories—some are places we've been, things we've shared, or moments that have defined our bond. Your task is to **unscramble** these words and guess what they are! Simple, right? 😜 But don't be fooled; these words have a deeper connection, and only someone who knows our story can solve them!

        🌟 **Why Scrabble?**  
        Well, because life is like a Scrabble game, isn’t it? We shuffle through moments, rearrange our thoughts, and sometimes stumble upon the perfect word (or memory) that scores the highest in our hearts. 💖🧠

        ✨ **Get ready to unscramble, reminisce, and maybe giggle a little at how our inside jokes and shared secrets have shaped these words!** Let’s see how well you remember all those little moments that make our bond so unique. 🤭🎈

        💪 **Let the Scrabble fun begin! And remember, every correct word brings you one step closer to unlocking your ultimate gift!** 🎁  
        
        ---
    """)
    
    # Scrambled words, hints, and answers
    scrambles = {
        "DHIBUD": ("A nickname Greeky uses for Arsh, meaning 'wise one.'", "buddhi"),
        "LEINH TAE HMEIV": ("A phrase in Punjabi often said by Arsh, meaning 'I am free.'", "mein te vehli"),
        "RAPOGIJ’SS HOESU": ("The cousin’s house where movie nights and bonding occurred.", "gopi's house"),
        "OTRNTOO": ("The city where a serious conversation was planned.", "toronto"),
        "CLGOAES": ("An item that Greeky gently removed while Arsh slept.", "glasses"),
        "DSRAOSUE": ("An item that got wet while cleaning dishes, causing some discomfort.", "trousers"),
        "TSWAPHAP": ("The platform where Greeky and Arsh often communicated and shared their feelings.", "whatsapp"),
        "VCONEROAU": ("The city where Greeky first met Arsh.", "vancouver"),
        "NTAOESRIPA": ("A phase in their friendship that represented a challenge of being apart.", "separation"),
        "SEPRKHOAT": ("A network connection Greeky asked to use at the Falls.", "hotspot"),
    }

    # Display scrambles and check answers
    correct_answers = 0
    for word, (hint, answer) in scrambles.items():
        st.write(f"**Scramble**: {word}")
        st.markdown(f"<small>**Hint:** {hint}</small>", unsafe_allow_html=True)
        user_answer = st.text_input(f"Your answer for {word}:", key=word)

        if user_answer.lower().strip() == answer:
            st.success("Correct! 🎉 You're doing great!")
            correct_answers += 1
        elif user_answer:
            st.error("Try again! 😅")
        
        # Add a horizontal line to separate each word section
        st.markdown("---")

    if correct_answers == len(scrambles):
        st.success("Congratulations! 🎊 You've unscrambled all the words! On to the next challenge! 🚀")
        st.button("Proceed to the Next Game", on_click=proceed_to_next_step, args=(4,))

# 4. Audio Guessing Game Section
def audio_guessing_game():
    st.title("🎵 Guess the Song: Audio Challenge! 🎶")
    st.markdown("""
        #### 🎧 Let's Test Your Knowledge of Your Favourite Artist, Diljit Dosanjh! 🎤  
        
        This next game is all about music, and who better to focus on than your favourite artist—**Diljit Dosanjh**! 🌟 His songs have been a big part of our journey, playing in the background during road trips, late-night chats, and those moments when we just needed a good beat to vibe to. 🕺💃

        Here's how this works:  
        - I've selected some of his hit songs, and you'll need to guess their titles!  
        - Listen to each audio clip and try to identify the song.  
        - For each song, I'll give you a hint: the **number of letters** in the song's name. But the rest is up to you! 🎧😉

        💡 **Hint:** Think about the lyrics, the beat, and the feeling you get when the song plays. Can you recall the name? Let’s see how well you know your Diljit Dosanjh playlist! 🎶

        Good luck, and may your musical instincts guide you! 🎵✨  
        ---
    """)

    # List of songs (hidden answers, use actual file paths for mp3 files)
    songs = [
        ('Daka', 'Daka.mp3', 4),  # (Answer, File, Number of letters)
        ('Lehnga', 'Lehnga.mp3', 6),
        ('Lemonade', 'Lemonade.mp3', 8),
        ('Strawberry', 'Strawberry.mp3', 10),
        ('Taare', 'Taare.mp3', 5),
        ('Vibe', 'Vibe.mp3', 4),
        ('Weekend', 'Weekend.mp3', 7),
        ('Champagne', 'Champagne.mp3', 9),
        ('Waheguru', 'Waheguru.mp3', 8),
        ('Pyar', 'Pyar.mp3', 4),
    ]

    # Check if the user guessed all songs correctly
    correct_songs = 0
    for song_name, song_file, letters_count in songs:
        st.audio(song_file, format='audio/mp3')
        st.markdown(f"<small>**Hint:** The song name has **{letters_count} letters**. 🎵</small>", unsafe_allow_html=True)
        answer = st.text_input("Guess the song name:", key=song_file)
        if answer.lower().strip() == song_name.lower():
            st.success("Correct! 🎉 You're on fire!")
            correct_songs += 1
        elif answer:
            st.error("Incorrect. Try again! 🤔")
        
        # Add a horizontal line to separate each song section
        st.markdown("---")

    if correct_songs == len(songs):
        st.success("Amazing! 🎊 You guessed all the songs correctly! You really know your Diljit Dosanjh hits! 🎧")
        st.button("Proceed to the Next Game", on_click=proceed_to_next_step, args=(5,))

# 5. Riddle Game Section
def riddle_game():
    st.title("🧩 Riddle Challenge: Things Are Getting Personal! 🤔")
    st.markdown("""
        #### 🎉 You're 50% Through the Treasure Hunt! Keep Going! 🌟  

        Congratulations, you've made it halfway through this exciting adventure! 🥳 Now, we're stepping things up a bit. From here on out, things are going to get a little more personal and maybe a bit more challenging too! 😜  

        This section is all about **riddles** that revolve around our special moments and unique memories. Each riddle is a little puzzle piece from our journey together, and only someone who truly knows these stories can solve them! 🧠💕

        Here's how it works:  
        - I'll present you with a riddle—each one crafted from our shared experiences.  
        - Your job is to read between the lines, think back to our times together, and figure out the answer.  
        - For each riddle, I'll give you a hint: the **first letter** of the answer and the **number of letters** in the answer.  

        🌈 **Are you ready to solve some riddles and unlock the next step in your quest?** Let's go! 🚀

        ---
    """)

    # Riddles, hints, and answers
    riddles = {
        "I’m a type of footwear that matched by fate, Both wore them at a second meeting date. What is the brand of these shoes that sealed the state?": ("nike", "N", 4),
        "The scent that stayed with us, simple yet strong, Reminds Greeky of love that’s lifelong. Name the shampoo fragrance that makes everything feel so right, not wrong.": ("pantene", "P", 7),
        "I’m the feeling that struck like a dart, When Greeky pulled a prank and touched your heart. What emotion did Greeky feel, one word that tore him apart?": ("regret", "R", 6),
        "A movie's name, where fear and thrills were abound, But it’s where two hands found each other without a sound. Your trousers were wet, but the moment was sweet, Name the movie where our hands first did meet.": ("annabelle", "A", 9),
        "An annual month that brought joy to its peak, Where laughter, bonding, and late-night chats were sleek. Which month hosted the second meet, a reunion so unique?": ("july", "J", 4)
    }

    # Display riddles and check answers
    correct_riddles = 0
    for riddle, (answer, first_letter, num_letters) in riddles.items():
        st.markdown(f"<small>**Riddle:** {riddle}</small>", unsafe_allow_html=True)
        st.markdown(f"<small>**Hint:** First letter is **'{first_letter}'** and the answer has **{num_letters} letters**.</small>", unsafe_allow_html=True)
        user_answer = st.text_input("Your answer:", key=riddle)

        if user_answer.lower().strip() == answer:
            st.success("Correct! 🎉 You're on a roll!")
            correct_riddles += 1
        elif user_answer:
            st.error("That's not right. Try again! 🤔")
        
        # Add a horizontal line to separate each riddle section
        st.markdown("---")

    if correct_riddles == len(riddles):
        st.success("Well done! 🎊 You've solved all the riddles! You're one step closer to the final treasure! 🚀")
        st.button("Proceed to the Final Part", on_click=proceed_to_next_step, args=(6,))

# 6. Final Question Series with the Oath
def final_questions():
    st.title("📝 Final Question Series: The Last Stretch! 🏁")
    st.markdown("""
        #### 🎉 You’re Almost There! Don’t Give Up Now! 🌟  

        Wow, Arshdeep! You’ve come so far in this treasure hunt, and you’re just one step away from unlocking the ultimate gift! 🎁 This is the final round, and it’s going to be a bit more challenging. But I believe in you! 💪  

        This section is packed with some tricky questions that only someone who knows our story inside out can answer. But don't worry, I’ve added some hints to guide you through. Just take your time, think back to our moments, and if you get stuck... well, you know who to call! 📞 Greeky is always here to help. 😜  

        Remember, every answer you give is a step closer to your special surprise. So stay focused, stay sharp, and let’s finish this strong! 💥

        ---
    """)

    # Questions, hints, and answers
    questions = {
        "How many pictures did I show of myself during the Eighth Shayari Phase?": ("19", "2 digits"),
        "Where did we create our first-ever Snapchat video together?": ("walmart", "7 letters"),
        "What nickname did we use when playing on the same team in Kahoot?": ("deep gang", "8 letters (2 words)"),
        "How many days after turning 18 did you move to Canada?": ("15", "2 digits"),
        "What is the title of our special song that we both cherish?": ("deep love me", "11 letters (3 words)"),
        "On what date did I first send you a message on Facebook Messenger?": ("10/12/2023", "Date format: DD/MM/YYYY"),
        "On which date did you tie Rakhri on my wrist?": ("29/07/2024", "Date format: DD/MM/YYYY")
    }

    # Display questions and check answers
    correct_answers = 0
    for question, (answer, hint) in questions.items():
        st.markdown(f"**Question:** {question}")
        st.markdown(f"<small>**Hint:** {hint}</small>", unsafe_allow_html=True)
        user_answer = st.text_input("Your answer:", key=question)

        if user_answer.lower().strip() == answer.lower():
            st.success("Correct! 🎉 You're almost at the finish line!")
            correct_answers += 1
        elif user_answer:
            st.error("That's not quite right. Think harder! 🤔")

        # Add a horizontal line to separate each question section
        st.markdown("---")

    if correct_answers == len(questions):
        st.balloons()
        st.success("Congratulations, Arsh! 🎂🥳 You've completed all the games and challenges! The final treasure is now yours to unlock! 🎁")

        # Proceed to the oath page
        st.button("Click here to proceed to the Oath of Everlasting Friendship and Love", on_click=proceed_to_next_step, args=(7,))

# 7. The Oath Page
def oath_page():
    st.title("The Oath of Everlasting Friendship and Love 🌹💖")
    st.markdown("""

    I, **AmanDeep Saini Singh**, also known as your **Greeky, Big Head, and Buddha** 🧘‍♂️🤓, do hereby take this solemn oath on this most special day—the 15th of September, 2024—to honor, cherish, and uphold the sacred bond that we share. This oath is not just a promise, but a declaration of my heart and soul 💞, dedicated to you, **Arsh Kaur**—my Arsh, my Ms. Unstoppable Radio 🎤, my Best Friend for Life 👫, my BBFE, and my Meri Buddhi 🧠.

    1. **To Always Be by Your Side**: I vow to stand beside you in every season of life, whether in joy 😄 or sorrow 😢, in triumph 🏆 or struggle 💪. I will be your unwavering support, your rock, your constant, no matter what life throws our way... When the world feels too heavy 🌏, know that my shoulders are strong enough to carry your burdens alongside my own.

    2. **To Cherish Our Bond Forever**: From the very first time we met, I felt a connection that words cannot fully describe—a bond that transcends time ⏳, distance ✈️, and circumstance 🌈. I promise to treasure this bond, to nurture it with love ❤️, trust 🤝, and understanding 🤍... Our memories are a treasure chest filled with our laughter 😂, our stories 📖, and our secrets 🤫.

    3. **To Be Open, Honest, and True**: I swear to always be honest with you 🗣️, to speak my truth even when it’s hard, and to listen with an open heart 💗. I will share my deepest thoughts, fears, dreams 🌠, and joys with you, trusting you as my closest confidant 💬...

    4. **To Make You Laugh and Lift You Up**: I vow to fill your life with laughter 😂, to bring a smile to your face 😄 even on the toughest days 🌧️. I will be the one to lift you up when you’re down 🙌, to remind you of your strength 💪 when you feel weak...

    5. **To Respect and Honor You Always**: I promise to respect your feelings 🤗, your thoughts 💭, and your boundaries 🚧. I will honor who you are and who you are becoming 🌱, supporting you in every decision you make...

    6. **To Create Memories That Last a Lifetime**: I swear to create a lifetime of memories with you—ones filled with joy 🎉, adventure 🚀, deep conversations ☕, and quiet moments of reflection 🌌...

    7. **To Never Let Insecurity or Doubt Separate Us**: I vow to trust in our friendship 👭, to believe in the strength of our bond, and to never let insecurity, doubt, or misunderstanding come between us 🌻...

    8. **To Be Your Forever Friend**: Above all, I swear to be your best friend for life 🌟. To love you, support you, and stand by you as long as I breathe 🌬️...

    This is my oath, my unbreakable promise to you, my dearest Arsh. I pledge to live up to this oath every day 🌞, to honor the love 💖 and friendship we have built, and to continue growing 🌿, laughing 😂, and living life to the fullest—together, always. For every sunrise 🌅 we see and every sunset 🌇 we miss, for every tear we shed 😢 and every laugh we share 😄, for all that we are and all that we will be—I will be there, bound by this oath, with all my heart and soul 💞.

    With all the love and strength within me, I take this oath today and forevermore. 🌹  
    Signed,  
    **Your Greeky, Big Head, and Buddha** 🧘‍♂️  
    **AmanDeep Saini Singh** ✍️
    """)

    # Button for downloading the special book
    st.markdown("---")
    st.markdown("<h3 style='text-align: center;'>🎁 Your Special Gift: Our Book! 🎁</h3>", unsafe_allow_html=True)
    
    # Big download button
    with open('Arshdeep.pdf', 'rb') as book_file:  # Replace 'your_book_path.pdf' with the actual path to your book file
        st.download_button(
            label="📖 Click Here to Download Your Special Book! 📖",
            data=book_file,
            file_name='Unbreakable_Bond.pdf',  # Customize the file name as needed
            mime='application/pdf',
            key='download-book',
        )

# 8. Footer - Define it here
def footer():
    st.markdown("---")
    st.markdown(
        """
        <div style="text-align: center;">
            <h5>🌟 Made with Love by Your Greeky, Big Head, Buddha 🌟</h5>
            <p>Arsh, wherever life takes us, I'm here—forever and always. 🤗💖</p>
            <p>~ Amandeep Saini Singh 👫💞</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
# Update the display logic to include the new oath page
if st.session_state.current_step == 1:
    authenticator()
elif st.session_state.current_step == 2:
    introduction()
elif st.session_state.current_step == 3:
    scrabble_game()
elif st.session_state.current_step == 4:
    audio_guessing_game()
elif st.session_state.current_step == 5:
    riddle_game()
elif st.session_state.current_step == 6:
    final_questions()
elif st.session_state.current_step == 7:
    oath_page()  # New oath page

# Add footer at the end of all sections
footer()


