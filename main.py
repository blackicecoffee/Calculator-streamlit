import streamlit as st

def create_btn(number, col, height=None, type="secondary"):
    btn_num = col.container(height=height)
    with btn_num:
        btn = st.button(number, key=f"{number}", use_container_width=True, type=type)
    return btn

def check_valid_float(param: str) -> bool:
    if param.count('.') > 1: 
        return True
    return False

_, main_col, _ = st.columns([0.2, 0.6, 0.2])

result = ""

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
            btn_ac = create_btn("AC", ac_col)
            if btn_ac:
                st.session_state["result"] = ""

        numCol1 = st.columns(4)
        numCol2 = st.columns(4)
        numCol3 = st.columns(4)
        numCol4 = st.columns(4)

        btn_7 = create_btn("7", numCol1[0])
        btn_8 = create_btn("8", numCol1[1])
        btn_9 = create_btn("9", numCol1[2])
        btn_div = create_btn("/", numCol1[3])

        btn_4 = create_btn("4", numCol2[0])
        btn_5 = create_btn("5", numCol2[1])
        btn_6 = create_btn("6", numCol2[2])
        btn_mul = create_btn("\*", numCol2[3])
        
        btn_1 = create_btn("1", numCol3[0])
        btn_2 = create_btn("2", numCol3[1])
        btn_3 = create_btn("3", numCol3[2])
        btn_minus = create_btn("\-", numCol3[3])

        btn_0 = create_btn("0", numCol3[0])
        btn_dot = create_btn(".", numCol3[1])
        btn_equal = create_btn("=", numCol3[2])
        btn_plus = create_btn('\+', numCol3[3])

        if btn_1:
            st.session_state["result"] += "1"
            inp_grid.text(st.session_state["result"])
        
        if btn_2:
            st.session_state["result"] += "2"
            inp_grid.text(st.session_state["result"])

        if btn_3:
            st.session_state["result"] += "3"
            inp_grid.text(st.session_state["result"])

        if btn_4:
            st.session_state["result"] += "4"
            inp_grid.text(st.session_state["result"])

        if btn_5:
            st.session_state["result"] += "5"
            inp_grid.text(st.session_state["result"])

        if btn_6:
            st.session_state["result"] += "6"
            inp_grid.text(st.session_state["result"])

        if btn_7:
            st.session_state["result"] += "7"
            inp_grid.text(st.session_state["result"])
        
        if btn_8:
            st.session_state["result"] += "8"
            inp_grid.text(st.session_state["result"])

        if btn_9:
            st.session_state["result"] += "9"
            inp_grid.text(st.session_state["result"])

        if btn_0:
            st.session_state["result"] += "0"
            inp_grid.text(st.session_state["result"])
        
        if btn_plus:
            if st.session_state["result"] == "":
                st.session_state["result"] += "+"
            else: st.session_state["result"] += " + "
            inp_grid.text(st.session_state["result"])

        if btn_minus:
            if st.session_state["result"] == "":
                st.session_state["result"] += "-"
            else: st.session_state["result"] += " - "
            inp_grid.text(st.session_state["result"])

        if btn_mul:
            st.session_state["result"] += " * "
            inp_grid.text(st.session_state["result"])

        if btn_div:
            st.session_state["result"] += " / "
            inp_grid.text(st.session_state["result"])

        if btn_dot:
            st.session_state["result"] += "."
            inp_grid.text(st.session_state["result"])

        if btn_equal:
            expr = st.session_state["result"]
            args = expr.split(" ")
            
            if (len(args) > 3):
                st.session_state["result"] = "TOO MANY ARGUMENTS"
                inp_grid.text(st.session_state["result"])
                st.session_state["result"] = ""
        
            else:
                if len(args) == 1:
                    if check_valid_float(args[0]) or args[0] in ["+", "-", "*", "/", "", "."]:
                        st.session_state["result"] = "INVALID"
                        inp_grid.text(st.session_state["result"])
                        st.session_state["result"] = ""
                    else:
                        st.session_state["result"] = str(float(args[0]))
                        inp_grid.text(st.session_state["result"])

                elif args[0] in ["+", "-", "*", "/", "", "."] or args[2] in ["+", "-", "*", "/", "", "."]:
                    st.session_state["result"] = "INVALID"
                    inp_grid.text(st.session_state["result"])
                    st.session_state["result"] = ""
   
                else:
                    if check_valid_float(args[0]) or check_valid_float(args[2]):
                        st.session_state["result"] = "INVALID"
                        inp_grid.text(st.session_state["result"])
                        st.session_state["result"] = ""
                    
                    else:
                        num1 = float(args[0])
                        op = args[1]
                        num2 = float(args[2])

                        if op == "+":
                            st.session_state["result"] = str(num1 + num2)
                            inp_grid.text(st.session_state["result"])

                        elif op == "-":
                            st.session_state["result"] = str(num1 - num2)
                            inp_grid.text(st.session_state["result"])
                            
                        elif op == "*":
                            st.session_state["result"] = str(num1 * num2)
                            inp_grid.text(st.session_state["result"])

                        elif op == "/":
                            if float(num2) == 0.0:
                                st.session_state["result"] = "INF"
                                inp_grid.text(st.session_state["result"])
                                st.session_state["result"] = ""
                            else:
                                st.session_state["result"] = str(num1 / num2)
                                inp_grid.text(st.session_state["result"])