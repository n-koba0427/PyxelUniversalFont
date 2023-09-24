import pyxel
import PyxelUniversalFont as puf

class App:
    def __init__(self) -> None:
        pyxel.init(500, 500)
        
        self.writers = puf.get_writers()
        
        self.text = "こんにちは、世界！"
        self.font_size = 32
        self.font_color = 0
        
        pyxel.run(self.update, self.draw)
        
    def update(self):
        pass
    
    def draw(self):
        pyxel.cls(7)
        
        for i, (font_name, writer) in enumerate(self.writers.items()):
            writer.draw(
                x = 0,
                y = i*(self.font_size+2),
                text = f"{font_name}:{self.text}",
                font_size = self.font_size,
                font_color = self.font_color,
                background_color = 7,
            )

def start_app():
    App()

if __name__ == "__main__": 
    start_app()