import gradio as gr
from pytubefix import YouTube

def download_video(link):
    try:
        yt = YouTube(link)
        # İndirilmek istenen video akışını seçme
        stream = yt.streams.filter(progressive=True, file_extension='mp4').first()

        if stream:
            stream.download()  # İndirme işlemi
            return f"{yt.title} başarıyla indirildi!"
        else:
            return "Video akışı bulunamadı. Lütfen farklı bir link deneyin."
    except Exception as e:
        return f"Hata oluştu: {str(e)}"

# Gradio arayüzü oluştur
interface = gr.Interface(
    fn=download_video,
    inputs=gr.Textbox(label="YouTube Video Linki"),
    outputs="text",
    title="YouTube Video İndirici",
    description="YouTube linkini girin ve MP4 formatında indirin.",

)

# Arayüzü başlat
interface.launch(share=True)
