import datetime
from application.salary import calculate_salary
from application.db.people import get_employees
from application.matrix import matrix

if __name__ == '__main__':
    now = datetime.datetime.now()
    print("Текущий год: %d" % now.year)
    print("Текущий месяц: %d" % now.month)
    print("Текущий день: %d" % now.day)
    print("Текущий час: %d" % now.hour)
    print("Текущая минута: %d" % now.minute)

    print(calculate_salary())
    print(get_employees())

    while True:
        matrix.screen.blit(matrix.surface, (0, 0))
        matrix.surface.fill(matrix.pg.Color('black'))

        [symbol_column.draw() for symbol_column in matrix.symbol_columns]

        if not matrix.pg.time.get_ticks() % 30 and matrix.alpha_value < 80:
            matrix.alpha_value += 1
            matrix.surface.set_alpha(matrix.alpha_value)

        [exit() for i in matrix.pg.event.get() if i.type == matrix.pg.QUIT]
        matrix.pg.display.flip()
        matrix.clock.tick(120)
