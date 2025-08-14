import uvicorn

from fastapi import FastAPI, HTTPException, status

app = FastAPI()


courses = {
    1: {
        "title": "Programing in Python",
        "classes": 112,
        "hours": 26
    },
    2: {
        "title": "Web Development with Django",
        "classes": 98,
        "hours": 32
    },
    3: {
        "title": "Data Science with Pandas",
        "classes": 80,
        "hours": 24
    },
    4: {
        "title": "Machine Learning with Scikit-learn",
        "classes": 120,
        "hours": 40
    },
    5: {
        "title": "Introduction to SQL",
        "classes": 60,
        "hours": 18
    }
}


@app.get('/courses')
async def get_courses():
    return courses

@app.get('/courses/{course_id}')
async def get_course(course_id: int):
    try:
        course = courses[course_id]
        course.update({'id': course_id})

        return course
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Not Found a course with this ID')

if __name__ == '__main__':

    uvicorn.run('main:app',
                host='localhost',
                port=8000,
                log_level='info',
                reload=True)