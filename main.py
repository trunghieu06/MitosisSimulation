from cell import *

def show_fps(x=10, y=40, color=(255, 255, 255)):
    """Hiển thị FPS ở góc màn hình"""
    fps_text = font.render(f"FPS: {int(clock.get_fps())}", True, color)
    SCREEN.blit(fps_text, (x, y))

def main():

    cells = []
    cells.append(Cell(pos=random_vector(100, WIDTH - 100, 100, HEIGHT - 100)))
    cells.append(Cell(pos=random_vector(100, WIDTH - 100, 100, HEIGHT - 100)))
    cells.append(Cell(pos=random_vector(100, WIDTH - 100, 100, HEIGHT - 100)))
    cells.append(Cell(pos=random_vector(100, WIDTH - 100, 100, HEIGHT - 100)))

    running = True
    while running:
        mouse_pos = np.array(pygame.mouse.get_pos(), dtype=np.float64)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for cell in reversed(cells):
                    if math.dist(mouse_pos, cell.pos) <= cell.r:
                        cells.append(cell.mitosis())
                        cells.append(cell.mitosis())
                        cells.remove(cell)
                        break

        SCREEN.fill((24, 24, 28))

        # Hiển thị kích thước lên góc trái
        txt = font.render(f"Size: {WIDTH} x {HEIGHT}  |  Esc to quit", True, (235, 235, 235))
        SCREEN.blit(txt, (10, 10))
        show_fps()

        for cell in cells:
            cell.show()
            cell.move()
            if cell.r < 60:
                cell.r = min(60, 1.0002 * cell.r)

        cursor_rect = cursor_img.get_rect(center=mouse_pos)
        SCREEN.blit(cursor_img, cursor_rect)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
