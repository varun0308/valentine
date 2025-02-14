import streamlit as st
import time
import pandas as pd
import numpy as np

def sad_func():
    _, c, _ = st.columns([1,4,1])
    with c:
        st.image("images/img4.png")
        
if "state" not in st.session_state:
    st.session_state['state'] = 0

# Login
if st.session_state['state'] == 0:
    st.header('Is this intended for you?')
    st.info("""Two clown in attire as bright as fresh snow,\n
Seated beside tracks where the urban heartbeat does flow.\n
They savored a dish, creamy and light—\n
A meal echoing the hue of their attire so white.\n

Then onward they wandered to a haven of sweet art,\n
Where desserts stirred memories and warmed the heart.\n
Recall the point of their delightful tour,\n
Which is believed to be in floor four""")
    with st.form('authentication'):
        answer = st.text_input('Answer to the riddle:')
        submit = st.form_submit_button('Check answer')
        
        if submit:
            a = answer.split()
            if len(a) == 2:
                if a[0].lower() == 'cafe' and a[1].lower() == 'azzure':
                    st.success('Hi babes!!! <3')
                    st.session_state['state'] = 1
                    with st.spinner('Hold on... Authorizing love missile...🚀🚀'):
                        time.sleep(3)
                        st.balloons()
                        time.sleep(2)
                        st.rerun()
                else:
                    st.error('Excuse me, who tf are you?')
            elif len(a) == 1:
                if a[0].lower().strip() == 'azzure':
                    st.success('Hi babes!!! <3')
                    st.session_state['state'] = 1
                    with st.spinner('Hold on... Authorizing love missile...🚀🚀'):
                        time.sleep(3)
                        st.balloons()
                        time.sleep(2)
                        st.rerun()
                else:
                    st.error('Excuse me, who tf are you?')
            else:
                st.info('Expecting max 2 words answer :(')

# Graph
if st.session_state['state'] == 1:
    # Set the title of the app
    st.title("My love for you - A graph ❤️")

    # Define the start and end dates
    start_date = "2022-08-03"
    end_date = "2025-02-14"

    # Generate weekly dates (every 7 days)
    dates = pd.date_range(start=start_date, end=end_date, freq="D")

    # Generate random data for the y-axis and compute a cumulative sum to simulate a trend
    love_percent = np.random.uniform(low=50, high=110, size=len(dates))
    raw_measure_series = pd.Series(love_percent, index=dates)

    manual_dates = [pd.to_datetime(d) for d in ["2022-08-03", "2022-10-21", "2023-02-14", "2023-03-24", "2023-02-14", "2023-05-28", "2023-08-03", "2023-09-22", "2023-10-21", "2024-01-01", "2024-02-14", "2024-02-18", "2024-06-18", "2024-06-23", "2024-08-03", "2024-09-22", "2024-10-21", "2025-01-01"]]
    for d in manual_dates:
        manual_date = pd.date_range(start=d, periods=5, freq="D")
        raw_measure_series.loc[manual_date] = np.random.randint(low=120, high=150)

    smoothed_love_percent = raw_measure_series.rolling(window=5, min_periods=1).mean().values
    # Create a DataFrame with Date as the index
    df = pd.DataFrame({"Love %": smoothed_love_percent}, index=dates)

    # Display the line chart in the Streamlit app
    st.line_chart(df, height=500)






    st.info("So what are these 'spiky' dates??")
    # Create a markdown bullet list
    bullet_points = "\n".join([f"- {str(x.date())}" for x in manual_dates])
    st.markdown(bullet_points)




    with st.expander("The graph looks somewhat off..."):
        st.subheader("Okayyy, whom am I kidding xD.")
        st.subheader("THIS is the real graph ❤️❤️")
        start_date = "2022-10-21"
        end_date = "2025-02-14"

        # Generate weekly dates between the start and end dates
        dates = list(pd.date_range(start=start_date, end=end_date, freq="1M"))

        # Generate smooth increasing values from 90 to 160
        x = np.linspace(0, 1, len(dates))

        # Use a non-linear transformation to create curvature.
        # For example, raising x to a power (alpha > 1 produces a concave-up curve)
        alpha = 2  # Adjust this value to change the curvature
        y = 90 + (300 - 90) * (x ** alpha)

        # Create a DataFrame with the dates as the index
        df = pd.DataFrame({"Measure": y}, index=dates)

        # Display the line chart in the Streamlit app
        st.line_chart(df)

        st.success("I never stopped loving you babe ❤️, just an increasing graph of pure love 📈❤️")
        
    if st.button("Next"):
        print(st.session_state['state'])
        st.session_state['state'] = 2
        print(st.session_state['state'])
        st.rerun()

# Pinpoint
if st.session_state['state'] == 2:
    if "q_num" not in st.session_state:
        st.session_state['q_num'] = 0
    if "attempts" not in st.session_state:
        st.session_state['attempts'] = 0
    if "game_over" not in st.session_state:
        st.session_state['game_over'] = 0
    st.title("Let's play Pinpoint")
    st.caption("""Disclaimer: I coudn't get good animations from streamlit as it doesn't support. Hope you still enjoy <3""")
    st.info("""I would've loved to play this everyday with you :( But alas the time difference. So here goes, I replicated Pinpoint for US""")
    st.divider()
    # Predefined answers and hints
    ANSWERS = ["Turtle", "Gokarna", "Polaroids", "21 Oct", "The times I have missed you :("]
    HINTS = [["Plushie", "Key chain", "Pant", "Another key chain?", "May 28th"],
                ["Tender coconut", "Did your parents know? Yes and No", "Baccardi", "3+1: The crime scene", "Pure seduction"],
                ["Airport goodbye", "Farewell", "Pondicherry", "Arundati's house", "Graduation"],
                ["Food adda (Ans is a date like: '28 May')", "The start line", "Vijaylakshmi coffee", "'I will actually tell after I come back'", "'So Gayatre... Now that SEEs are over'"],
                ["~8 months", "Whole weeks", "Yesterday... The whole day", "Today morning", "Right now"]]

    if st.session_state.q_num < len(ANSWERS):
        if st.session_state.q_num == len(ANSWERS) - 1:
            st.caption("Don't overthink this question :)")
        revealed_hints = HINTS[st.session_state.q_num][:st.session_state.attempts + 1]
        
        _, c, _ = st.columns([1,3,1])
        with c:
            for idx, hint in enumerate(revealed_hints):
                st.info(f"**Hint {idx+1}:** {hint}")
            for idx in range(st.session_state.attempts + 1, 5):
                st.info(" ")

        if st.session_state.game_over == -1:
            st.error(f"Game Over! The correct answer was: **{ANSWERS[st.session_state.q_num]}**")
        elif st.session_state.game_over == 1:
            st.success(f"Congratulations! You guessed correctly: **{ANSWERS[st.session_state.q_num]}**")
        else:
            # Use a form so the page doesn't refresh on every keystroke.
            with st.form(key=f"guess_form_{st.session_state.q_num}"):
                guess = st.text_input("Enter your guess:")
                submit = st.form_submit_button("Submit")

            if submit:
                # Standardize the guess to lower case and remove extra spaces
                if guess.lower().strip() == ANSWERS[st.session_state.q_num].lower():
                    st.success("Congratulations! You guessed correctly.")
                    st.session_state.attempts = 5
                    st.session_state.game_over = 1
                    st.rerun()
                else:
                    st.error("Wrong guess, try again!")
                    # Reveal the next hint if available.
                    if st.session_state.attempts < len(HINTS[st.session_state.q_num]) - 1:
                        st.session_state.attempts += 1
                        print(st.session_state.attempts)
                        st.rerun()
                    else:
                        if st.session_state.q_num == len(ANSWERS) - 1:
                            st.error("You'll never guess this")
                            st.error(f"The correct answer was: {ANSWERS[st.session_state.q_num]}")
                            st.session_state.attempts = 5
                            st.session_state.game_over = -1
                            st.rerun()
                            
                        else:
                            # All hints have been revealed. End the game.
                            st.error(f"Game Over! The correct answer was: **{ANSWERS[st.session_state.q_num]}**")
                            st.session_state.attempts = 5
                            st.session_state.game_over = -1
                            st.rerun()
                        
        
        if st.button("Next"):
            st.session_state.q_num += 1
            st.session_state.game_over = 0
            st.session_state.attempts = 0
            if st.session_state.q_num == len(ANSWERS):
                st.session_state.state = 3
            st.rerun()

# Ask out
if st.session_state['state'] == 3:
    # Actual ask out
    st.success('So here we are babe..... Almost 2.5 years in, a bunch of ups and downs along the way but still standing strong. I would sleep late for you, stare at my phone for hours waiting for your texts and will wait for YOU to come back. With all the hungama in life, the only time I look forward to in the day is the call with you, just to be myself for an hour or two❤️❤️')
    st.warning("I might be irritated by you, angry at you, pissed off at you, but I'll never stop loving you ❤️")
    st.success('We are dating, but it would be a crime to not ask you to be my valentine...')
    
    with st.expander("Click me!"):
        _, c, _ = st.columns([1,1,1])
        with c:
            st.image("images/img5.png", width=200)
        
        st.success('So dear babe, will you be my Valentine?')
        c_1, _, c_2 = st.columns([1,4,1])
        with c_1:
            no_btn = st.button('No', on_click=sad_func)
        with c_2:
            yes_btn = st.button('Yes')

        if yes_btn:
            st.session_state['state'] = 4
            st.rerun()

if st.session_state['state'] == 4:
    # Some celebration
    _, c, _ = st.columns([1,4,1])
    with c:
        st.image("images/img2.png")
    st.balloons()
    st.success("Happy Valentine's day ❤️❤️❤️")
    pass