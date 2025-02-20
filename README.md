![Poster](docs/_static/poster.png)

## Package Documentation

The documentation for the SpectAcoular package is available at [https://acoular.github.io/spectacoular/](https://acoular.github.io/spectacoular/).

## Quick Start

**SpectAcoular** is available on conda. In the command line, type:

```console
$ conda install -c acoular spectacoular
```

This will install SpectAcoular in your Anaconda Python environment and make the SpectAcoular library available from Python. In addition, this will install all dependencies (those other packages mentioned above) if they are not already present on your system.

To verify your installation, one can run one of the pre-build interactive applications (e.g. MicGeomExample app). To do so, navigate to the spectacoular/apps directory and type the following command in a dedicated console (e.g. shell):

```console
$ bokeh serve --show MicGeomExample
```

A new window should appear in the browser running the application.

## Project Description

SpectAcoular is built on top of Acoular and offers additional modules to further simplify the handling of Acoular. It implements interactive controls (widgets) for building individual graphical user interfaces with the visualization library Bokeh. Bokeh uses web browsers for visualization, whereby rendering and event handling is performed by a high-level JavaScript library. This allows creating real-time applications and using the capabilities of Acoular independently from the operating system. In addition, building client-server applications is supported, which makes it possible to interactively control microphone array data processing in a distributed scenario.

### Key Features

- Independent from operating system
- Tools for microphone array data acquisition, analysis, and exploration
- Individual client-server applications with interactive visualization
- Easily expandable interface to meet the requirements of flexible software design with custom processing

## Installation and Setup

To install SpectAcoular, follow these steps:

1. Ensure you have Anaconda installed on your system. If not, download and install it from [https://www.anaconda.com/download/](https://www.anaconda.com/download/).
2. Open a command line interface (e.g., cmd, Anaconda command prompt, Terminal).
3. Type the following command to install SpectAcoular:

```console
$ conda install -c acoular spectacoular
```

This will install SpectAcoular and its dependencies in your Anaconda Python environment.

## Running the Project and Applications

To run one of the pre-built interactive applications, follow these steps:

1. Navigate to the `spectacoular/apps` directory in your command line interface.
2. Type the following command to run the MicGeomExample app:

```console
$ bokeh serve --show MicGeomExample
```

A new window should appear in your browser running the application.

You can explore other applications in the `spectacoular/apps` directory by replacing `MicGeomExample` with the desired application name in the command above.
