import pyxel
import PyxelUniversalFont as puf

class App:
    def __init__(self) -> None:
        pyxel.init(500, 100)
        
        # フォントを指定
        self.writer = puf.Writer("IPA_Gothic")
        
        pyxel.run(self.update, self.draw)
        
    def update(self):
        pass
    
    def draw(self):
        pyxel.cls(7)

        # draw(x座標, y座標, テキスト, フォントサイズ, 色, 背景色)
        self.writer.draw(0, 0, "こんにちは、世界！", 48, 0, 7)

if __name__ == "__main__": 
    App()