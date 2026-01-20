import render

if __name__ == '__main__':
    try:
        render.render_scene()
    except KeyboardInterrupt:
        print("\nZakończono renderowanie.")

