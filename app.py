import gradio as gr
import traceback


def hello_world_fn(username: str) :
    try:
        return f"HELLO WORLD\n{username.upper()}", "SUCCESS"
    except Exception as e:
        return f"opus! some exception {e}\n{traceback.format_exc()}", "FAILED"


def main() -> None:
    with gr.Blocks(title="DeepLang Data test project") as demo:
        with gr.Tab("hello world 0"):
            raw_input = gr.Textbox(lines=1, placeholder="输入你的名字(英文)", label="")
            pack_output = gr.Textbox(label="输出")
            status_output = gr.Textbox(label="状态信息")

            btn = gr.Button("开始转换")
            btn.click(
                fn=hello_world_fn,
                inputs=raw_input,
                outputs=[pack_output, status_output],
            )

        with gr.Tab("hello world 1"):
            raw_input = gr.Textbox(lines=1, placeholder="输入你的名字(英文)", label="")
            pack_output = gr.Textbox(label="输出")
            status_output = gr.Textbox(label="状态信息")

            btn = gr.Button("开始转换")
            btn.click(
                fn=hello_world_fn,
                inputs=raw_input,
                outputs=[pack_output, status_output],
            )

        with gr.Tab("页面解析"):
            raw_input = gr.Textbox(lines=1, placeholder="输入你的名字(英文)", label="")
            pack_output = gr.Textbox(label="输出")
            status_output = gr.Textbox(label="状态信息")
            # raw_input = dealStr(raw_input)
            print(raw_input)
            btn = gr.Button("开始转换")
            btn.click(
                fn=dealStr,
                inputs=raw_input,
                outputs=[pack_output],
            )

    demo.queue(default_concurrency_limit=100).launch(
        inline=False,
        debug=False,
        server_name="127.0.0.1",
        server_port=8081,
        show_error=True,
    )

def dealStr(s: str) -> str:
    res = ''
    flag = 0
    # s = s.strip()
    s = s.split('\n')
    for line in s:
        line = line.strip();
        if '<p>' in line and '</p>' in line:
            res += line.split('<p>')[1].split("</p>")[0] + '\n'
            continue
        elif '<p>' in line:
            flag = 1
            continue
        elif flag == 1 and '</p>' in line:
            flag = 0
            continue
        elif flag == 1:
            if '<c>' in line:
                continue
            else:
                res += line + '\n'
    return res


if __name__ == "__main__":
    main()
