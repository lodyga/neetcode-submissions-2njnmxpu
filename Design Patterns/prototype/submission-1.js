class Shape {
    /**
     * @return {Shape}
     */
    clone() {}
}

/**
 * @param {number} width
 * @param {number} height
 * @return {Rectangle}
 */
class Rectangle extends Shape {
    constructor(width, height) {
        super();
        this.width = width;
        this.height = height;
    }

    /**
     * @return {number}
     */
    getWidth() {
        return this.width;
    }

    /**
     * @return {number}
     */
    getHeight() {
        return this.height;
    }

    /**
     * @return {Shape}
     */
    clone() {
        return new Rectangle(this.width, this.height)
    }
}

/**
 * @param {number} length
 * @return {Square}
 */
class Square extends Shape {
    constructor(length) {
        super();
        this.length = length;
    }

    /**
     * @return {number}
     */
    getLength() {
        return this.length;
    }

    /**
     * @return {Shape}
     */
    clone() {
        return new Square(this.length)
    }
}

class Test {
    /**
     * @param {Shape[]} shapes
     * @return {Shape[]}
     */
    cloneShapes(shapes) {
        const clonedShapes = [];
        shapes.forEach(shape => {
            clonedShapes.push(shape.clone())
        })

        return clonedShapes
    }
}
