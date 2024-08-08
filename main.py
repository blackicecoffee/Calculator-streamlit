import streamlit as st

def create_btn_number(number, col, height=None):
    btn_num = col.container(height=height)
    with btn_num:
        btn = st.button(number, key=f"{number}", use_container_width=True)
    return btn

_, main_col, _ = st.columns([0.2, 0.6, 0.2])

with main_col:

    main_container = st.container(border = True)

    with main_container:
        st.header("My simple calculator")

        inp_col, ac_col = st.columns([0.7, 0.3])
        with inp_col:
            inp_container = st.container(border=True)
            with inp_container:
                inp_grid = st.empty()
                inp_grid.text("0")
        
        with ac_col:
            btn_ac = create_btn_number("AC", ac_col)
            if btn_ac:
                inp_grid.text("0")

        numCol1 = st.columns(4)
        numCol2 = st.columns(4)
        numCol3 = st.columns(4)
        numCol4 = st.columns(4)

        btn_7 = create_btn_number("7", numCol1[0])
        btn_8 = create_btn_number("8", numCol1[1])
        btn_9 = create_btn_number("9", numCol1[2])
        btn_div = create_btn_number("/", numCol1[3])

        btn_4 = create_btn_number("4", numCol2[0])
        btn_5 = create_btn_number("5", numCol2[1])
        btn_6 = create_btn_number("6", numCol2[2])
        btn_mul = create_btn_number("*", numCol2[3])
        
        btn_1 = create_btn_number("1", numCol3[0])
        btn_2 = create_btn_number("2", numCol3[1])
        btn_3 = create_btn_number("3", numCol3[2])
        btn_minus = create_btn_number("-", numCol3[3])

        btn_0 = create_btn_number("0", numCol3[0])
        btn_dot = create_btn_number(".", numCol3[1])
        btn_equal = create_btn_number("=", numCol3[2])
        btn_plus = create_btn_number('+', numCol3[3])