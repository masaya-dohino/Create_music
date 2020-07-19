{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "SLSTM1.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "accelerator": "GPU"
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/masaya-dohino/Create_music/blob/master/SLSTM1.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "UM2xxXKFsIvj",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 70
        },
        "outputId": "2169f756-d62e-480b-8e3e-e6267024186d"
      },
      "source": [
        "!pip install torch"
      ],
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Requirement already satisfied: torch in /usr/local/lib/python3.6/dist-packages (1.5.1+cu101)\n",
            "Requirement already satisfied: numpy in /usr/local/lib/python3.6/dist-packages (from torch) (1.18.5)\n",
            "Requirement already satisfied: future in /usr/local/lib/python3.6/dist-packages (from torch) (0.16.0)\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "w6syeshosdEp",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "import torch\n",
        "import torch.nn as nn"
      ],
      "execution_count": 3,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "aaOSXXEZFYz_",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 406
        },
        "outputId": "fcbcb969-cf30-42db-c1ff-2be82840fad7"
      },
      "source": [
        "!pip install pypianoroll"
      ],
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Collecting pypianoroll\n",
            "  Downloading https://files.pythonhosted.org/packages/17/93/cca689c3e7f217a4a1906f6b96e81c4d57d423ff6778dcc7af3bad11c638/pypianoroll-0.5.3.tar.gz\n",
            "Requirement already satisfied: six<2.0,>=1.0.0 in /usr/local/lib/python3.6/dist-packages (from pypianoroll) (1.12.0)\n",
            "Requirement already satisfied: numpy<2.0,>=1.10.0 in /usr/local/lib/python3.6/dist-packages (from pypianoroll) (1.18.5)\n",
            "Requirement already satisfied: scipy<2.0,>=1.0.0 in /usr/local/lib/python3.6/dist-packages (from pypianoroll) (1.4.1)\n",
            "Collecting pretty_midi<1.0,>=0.2.8\n",
            "\u001b[?25l  Downloading https://files.pythonhosted.org/packages/bc/8e/63c6e39a7a64623a9cd6aec530070c70827f6f8f40deec938f323d7b1e15/pretty_midi-0.2.9.tar.gz (5.6MB)\n",
            "\u001b[K     |████████████████████████████████| 5.6MB 4.0MB/s \n",
            "\u001b[?25hCollecting mido>=1.1.16\n",
            "\u001b[?25l  Downloading https://files.pythonhosted.org/packages/20/0a/81beb587b1ae832ea6a1901dc7c6faa380e8dd154e0a862f0a9f3d2afab9/mido-1.2.9-py2.py3-none-any.whl (52kB)\n",
            "\u001b[K     |████████████████████████████████| 61kB 9.5MB/s \n",
            "\u001b[?25hBuilding wheels for collected packages: pypianoroll, pretty-midi\n",
            "  Building wheel for pypianoroll (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Created wheel for pypianoroll: filename=pypianoroll-0.5.3-cp36-none-any.whl size=23827 sha256=3f638903806e903aebecbf439960e945f1470397c3ea54480c1551fed0748541\n",
            "  Stored in directory: /root/.cache/pip/wheels/29/c8/c0/7b240ab723c2f96b03391796bdf278de513eabf1dfb989c07f\n",
            "  Building wheel for pretty-midi (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Created wheel for pretty-midi: filename=pretty_midi-0.2.9-cp36-none-any.whl size=5591953 sha256=ea99352d92e3695bc3c8717c7d922bc92916d9178d18ac70cd8212ef0805d176\n",
            "  Stored in directory: /root/.cache/pip/wheels/4c/a1/c6/b5697841db1112c6e5866d75a6b6bf1bef73b874782556ba66\n",
            "Successfully built pypianoroll pretty-midi\n",
            "Installing collected packages: mido, pretty-midi, pypianoroll\n",
            "Successfully installed mido-1.2.9 pretty-midi-0.2.9 pypianoroll-0.5.3\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "uomTDKUwFglw",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "339c52ca-a030-4ec7-864c-7368275992cf"
      },
      "source": [
        "!cd drive/My\\ Drive"
      ],
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "/bin/bash: line 0: cd: drive/My Drive: No such file or directory\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "m_wIMGVtF1zG",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "filename = \"drive/My Drive/music/dataset/aine.wav.mid\""
      ],
      "execution_count": 6,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "QaQ0OFUFdDcB",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 125
        },
        "outputId": "66c1708f-244b-4dc8-d5b0-35a7ab003b9f"
      },
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/drive')"
      ],
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Go to this URL in a browser: https://accounts.google.com/o/oauth2/auth?client_id=947318989803-6bn6qk8qdgf4n4g3pfee6491hc0brc4i.apps.googleusercontent.com&redirect_uri=urn%3aietf%3awg%3aoauth%3a2.0%3aoob&response_type=code&scope=email%20https%3a%2f%2fwww.googleapis.com%2fauth%2fdocs.test%20https%3a%2f%2fwww.googleapis.com%2fauth%2fdrive%20https%3a%2f%2fwww.googleapis.com%2fauth%2fdrive.photos.readonly%20https%3a%2f%2fwww.googleapis.com%2fauth%2fpeopleapi.readonly\n",
            "\n",
            "Enter your authorization code:\n",
            "··········\n",
            "Mounted at /content/drive\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "yevwj2UHGKod",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 105
        },
        "outputId": "35f385e5-ae6e-4343-d7df-ececd65c332b"
      },
      "source": [
        "import pypianoroll\n",
        "pianoroll = pypianoroll.parse(filename, beat_resolution=24, name='unknown')"
      ],
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Imageio: 'ffmpeg-linux64-v3.3.1' was not found on your computer; downloading it now.\n",
            "Try 1. Download from https://github.com/imageio/imageio-binaries/raw/master/ffmpeg/ffmpeg-linux64-v3.3.1 (43.8 MB)\n",
            "Downloading: 8192/45929032 bytes (0.0%)\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b1187840/45929032 bytes (2.6%)\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b3579904/45929032 bytes (7.8%)\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b6930432/45929032 bytes (15.1%)\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b10960896/45929032 bytes (23.9%)\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b15253504/45929032 bytes (33.2%)\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b19095552/45929032 bytes (41.6%)\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b23445504/45929032 bytes (51.0%)\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b27688960/45929032 bytes (60.3%)\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b32014336/45929032 bytes (69.7%)\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b36134912/45929032 bytes (78.7%)\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b40452096/45929032 bytes (88.1%)\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b44793856/45929032 bytes (97.5%)\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b45929032/45929032 bytes (100.0%)\n",
            "  Done\n",
            "File saved as /root/.imageio/ffmpeg/ffmpeg-linux64-v3.3.1.\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "E8WQQiSpGlSv",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "b58fcf70-4b05-4398-b99f-7f351e26badd"
      },
      "source": [
        "import numpy as np\n",
        "a1 = pianoroll.get_merged_pianoroll()\n",
        "a1 = np.array(a1)\n",
        "np.shape(a1)\n",
        "a1 = a1[:2832, :]\n",
        "np.shape(a1)"
      ],
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(2832, 128)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 9
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "jUQv-FQnHMx1",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "9b887aff-ca54-40f8-bb69-62c5b0c855ba"
      },
      "source": [
        "filename = \"drive/My Drive/music/dataset/flam.wav.mid\"\n",
        "import pypianoroll\n",
        "pianoroll = pypianoroll.parse(filename, beat_resolution=24, name='unknown')\n",
        "import numpy as np\n",
        "a2 = pianoroll.get_merged_pianoroll()\n",
        "a2 = np.array(a2)\n",
        "np.shape(a2)\n"
      ],
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(2832, 128)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 10
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Wi3Hpd7yHcXp",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "409d47c2-6fa5-4d40-8f67-77b226fb3b68"
      },
      "source": [
        "filename = \"drive/My Drive/music/dataset/lemon.wav.mid\"\n",
        "import pypianoroll\n",
        "pianoroll = pypianoroll.parse(filename, beat_resolution=24, name='unknown')\n",
        "import numpy as np\n",
        "a3 = pianoroll.get_merged_pianoroll()\n",
        "a3 = np.array(a3)\n",
        "np.shape(a3)\n",
        "a3 = a3[:2832, :]\n",
        "np.shape(a3)"
      ],
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(2832, 128)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 11
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "GLp3pWtgHmG2",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "4e3fb35e-875c-405d-e3c2-9ddb382546aa"
      },
      "source": [
        "filename = \"drive/My Drive/music/dataset/lose.wav.mid\"\n",
        "import pypianoroll\n",
        "pianoroll = pypianoroll.parse(filename, beat_resolution=24, name='unknown')\n",
        "import numpy as np\n",
        "a4 = pianoroll.get_merged_pianoroll()\n",
        "a4 = np.array(a4)\n",
        "np.shape(a4)\n",
        "a4 = a4[:2832, :]\n",
        "np.shape(a4)"
      ],
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(2832, 128)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 12
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "iouR1SPPHs6Z",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "60ca80f6-d50c-4257-f3d5-37b15c3d183f"
      },
      "source": [
        "\n",
        "filename = \"drive/My Drive/music/dataset/metro.wav.mid\"\n",
        "import pypianoroll\n",
        "pianoroll = pypianoroll.parse(filename, beat_resolution=24, name='unknown')\n",
        "import numpy as np\n",
        "a5 = pianoroll.get_merged_pianoroll()\n",
        "a5 = np.array(a5)\n",
        "a5 = a5[:2832, :]\n",
        "np.shape(a5)"
      ],
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(2832, 128)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 13
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Jw8S8b18Hz2U",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "d8ee561e-67b6-49ab-f5aa-ce7510dbcb0f"
      },
      "source": [
        "filename = \"drive/My Drive/music/dataset/peace.wav.mid\"\n",
        "import pypianoroll\n",
        "pianoroll = pypianoroll.parse(filename, beat_resolution=24, name='unknown')\n",
        "import numpy as np\n",
        "a6= pianoroll.get_merged_pianoroll()\n",
        "a6 = np.array(a6)\n",
        "a6 = a6[:2832, :]\n",
        "np.shape(a6)"
      ],
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(2832, 128)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 14
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "lEAiKiyqH-24",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "58173625-67fe-452c-9f53-ec054c2417d7"
      },
      "source": [
        "filename = \"drive/My Drive/music/dataset/uma.wav.mid\"\n",
        "import pypianoroll\n",
        "pianoroll = pypianoroll.parse(filename, beat_resolution=24, name='unknown')\n",
        "import numpy as np\n",
        "a7 = pianoroll.get_merged_pianoroll()\n",
        "a7 = np.array(a7)\n",
        "a7 = a7[:2832, :]\n",
        "np.shape(a7)"
      ],
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(2832, 128)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 15
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "8IepnhYuID7F",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "7a314ffa-f222-4c5c-e282-fdd8d71f44d2"
      },
      "source": [
        "filename = \"drive/My Drive/music/dataset/lemon.wav.mid\"\n",
        "import pypianoroll\n",
        "pianoroll = pypianoroll.parse(filename, beat_resolution=24, name='unknown')\n",
        "import numpy as np\n",
        "a8 = pianoroll.get_merged_pianoroll()\n",
        "a8 = np.array(a8)\n",
        "a8 = a8[:2832, :]\n",
        "np.shape(a8)"
      ],
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(2832, 128)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 16
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "CWudnZ3UGhPN",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 276
        },
        "outputId": "99a49d69-088c-4b14-bb23-de12cee56622"
      },
      "source": [
        "\n",
        "import numpy as np\n",
        "from pypianoroll import Multitrack, Track\n",
        "from matplotlib import pyplot as plt\n",
        "\n",
        "# Create a pianoroll matrix, where the first and second axes represent time\n",
        "# and pitch, respectively, and assign a C major chord to the pianoroll\n",
        "\n",
        "\n",
        "# Create a `pypianoroll.Track` instance\n",
        "track = Track(pianoroll=a1, program=0, is_drum=False,\n",
        "              name='my awesome piano')\n",
        "\n",
        "# Plot the pianoroll\n",
        "fig, ax = track.plot()\n",
        "plt.show()"
      ],
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "vLBaslbGNVt9",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 175
        },
        "outputId": "b5b3da62-7a67-46ca-ff28-9ccbd8627253"
      },
      "source": [
        "a1 = np.transpose(a1)\n",
        "print(np.shape(a1))\n",
        "aa1 = np.argmax(a1, axis=0)\n",
        "print(np.shape(aa1))\n",
        "a2 = np.transpose(a2)\n",
        "print(np.shape(a2))\n",
        "aa2 = np.argmax(a2, axis=0)\n",
        "a3 = np.transpose(a3)\n",
        "print(np.shape(a3))\n",
        "aa3 = np.argmax(a3, axis=0)\n",
        "a4 = np.transpose(a4)\n",
        "print(np.shape(a4))\n",
        "aa4 = np.argmax(a4, axis=0)\n",
        "a5 = np.transpose(a5)\n",
        "print(np.shape(a5))\n",
        "aa5 = np.argmax(a5, axis=0)\n",
        "a6 = np.transpose(a6)\n",
        "print(np.shape(a6))\n",
        "aa6 = np.argmax(a6, axis=0)\n",
        "a7 = np.transpose(a7)\n",
        "print(np.shape(a7))\n",
        "aa7 = np.argmax(a7, axis=0)\n",
        "a8 = np.transpose(a8)\n",
        "print(np.shape(a8))\n",
        "aa8 = np.argmax(a8, axis=0)\n"
      ],
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "(128, 2832)\n",
            "(2832,)\n",
            "(128, 2832)\n",
            "(128, 2832)\n",
            "(128, 2832)\n",
            "(128, 2832)\n",
            "(128, 2832)\n",
            "(128, 2832)\n",
            "(128, 2832)\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "VwgicWd-bz6L",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "dataset = [aa1,aa2,aa3,aa4,aa5,aa6,aa7,aa8]"
      ],
      "execution_count": 19,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "yTB1dlUs4xqm",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "#Stacked LSTM Model\n",
        "pitch_size = 128\n",
        "em_size = 64\n",
        "hidden_size = 64\n",
        "class StackedLSTM(nn.Module):\n",
        "  def __init__(self):\n",
        "    super(StackedLSTM, self).__init__()\n",
        "    self.em = nn.Embedding(pitch_size, em_size)\n",
        "    self.lstm = nn.LSTM(em_size, hidden_size, 4, batch_first=True)\n",
        "    self.linear = nn.Linear(hidden_size, pitch_size)\n",
        "    self.softmax = nn.Softmax()\n",
        "\n",
        "  def forward(self, ot, ht, ct):\n",
        "    ot = self.em(ot)\n",
        "\n",
        "    if sos == 0:\n",
        "      ott, (htt, ctt) = self.lstm(ot)\n",
        "    if sos == 1:\n",
        "      ott, (htt, ctt) = self.lstm(ot, (ht, ct))\n",
        "    \n",
        "    ott = ott.view(1, 64)\n",
        "    ott = self.softmax(self.linear(ott))\n",
        "\n",
        "    return ott, htt, ctt\n",
        "\n",
        "sLSTM = StackedLSTM()\n",
        "sLSTM = sLSTM.cuda()"
      ],
      "execution_count": 20,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "EQ0ET_3f-RP1",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "379d5d24-a1f4-420d-bee3-58f884b15977"
      },
      "source": [
        "global sos\n",
        "sos = 1\n",
        "ot = torch.randint(128, (1, 1))\n",
        "ht = torch.rand(4, 1, 64)\n",
        "ct = torch.rand(4, 1, 64)\n",
        "\n",
        "ot = ot.cuda()\n",
        "ht = ht.cuda()\n",
        "ct = ct.cuda()\n",
        "\n",
        "ott, htt, ctt = sLSTM(ot, ht, ct)\n",
        "print(ott.size(), htt.size(), ctt.size())"
      ],
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "torch.Size([1, 128]) torch.Size([4, 1, 64]) torch.Size([4, 1, 64])\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "zLmZt9kpK3-N",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "criterion = nn.CrossEntropyLoss()\n",
        "import torch.optim as optim\n",
        "lr = 0.01\n",
        "optimizer = optim.Adam(sLSTM.parameters(), lr=lr)"
      ],
      "execution_count": 22,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "VgzslofJNzRv",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "fb3d3393-260d-41bb-fc39-463c0a00cc6d"
      },
      "source": [
        "i = np.random.randint(0, 8)\n",
        "i"
      ],
      "execution_count": 23,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "6"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 23
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "5K7xoGYN_FNM",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "device = torch.device('cpu')\n",
        "tanh = nn.Tanh()\n",
        "\n",
        "def train():\n",
        "  sLSTM.train()\n",
        "  i = np.random.randint(0, 8)\n",
        "  train_data = dataset[i]\n",
        "  train_data = np.array(train_data, dtype='float32')\n",
        "  train_data = torch.from_numpy(train_data).clone()\n",
        "  train_data = train_data.cuda()\n",
        "  train_data = train_data.view(2832, 1)\n",
        "\n",
        "  global sos\n",
        "  loss = 0\n",
        "  seq = []\n",
        "\n",
        "  for i in range(2832):\n",
        "    y_train = train_data[i]\n",
        "    y_train = y_train.long()\n",
        "    if i == 0:\n",
        "      sos = 0\n",
        "      ot = torch.randint(1, (1, 1))\n",
        "      ht = torch.rand(4, 1, 64)\n",
        "      ct = torch.rand(4, 1, 64)\n",
        "\n",
        "      ot = ot.cuda()\n",
        "      ht = ht.cuda()\n",
        "      ct = ct.cuda()\n",
        "\n",
        "      ot, ht, ct = sLSTM(ot, ht, ct)\n",
        "      sos = 1\n",
        "    else:\n",
        "      ot, ht, ct = sLSTM(ot, ht, ct)\n",
        "\n",
        "    ott = torch.tensor(ot, requires_grad=True)\n",
        "    ott = ot.view(1, 128)\n",
        "    loss_i = criterion(ott, y_train)\n",
        "    loss += loss_i \n",
        "    #loss = loss / 2832\n",
        "    ot = ot.argmax()\n",
        "    ot = ot.view(1, 1)\n",
        "\n",
        "    \n",
        "\n",
        "    output = ott.argmax()\n",
        "    output = output.to(device)\n",
        "    output = output.detach().clone().numpy()\n",
        "    seq.append(output)\n",
        "\n",
        "  loss.backward()\n",
        "  optimizer.step()\n",
        "\n",
        "  return loss.item(), seq"
      ],
      "execution_count": 24,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "1CvoVLSRWXZi",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        },
        "outputId": "e696d018-e544-4975-d78c-fbbee726a766"
      },
      "source": [
        "epochs = 100\n",
        "train_history = []\n",
        "\n",
        "for epoch in range(epochs):\n",
        "  \n",
        "  train_loss, seq = train()\n",
        "  seq = np.reshape(seq, (2832, ))\n",
        "  train_history.append(train_loss)\n",
        "\n",
        "  print(f'[Epoch {epoch+1:3d}/{epochs:3d}]' \\\n",
        "          f' train_loss: {train_loss:.5f}')\n",
        "  print(seq)\n"
      ],
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[Epoch   1/100] train_loss: 13740.93164\n",
            "[101 101 101 ... 101 101 101]\n",
            "[Epoch   2/100] train_loss: 13739.92773\n",
            "[101  63  63 ...  63  63  63]\n",
            "[Epoch   3/100] train_loss: 13730.69531\n",
            "[70 63 63 ... 63 63 63]\n",
            "[Epoch   4/100] train_loss: 13722.02734\n",
            "[63 63 63 ... 63 63 63]\n",
            "[Epoch   5/100] train_loss: 13679.22070\n",
            "[63 63 63 ... 63 63 63]\n",
            "[Epoch   6/100] train_loss: 13694.88672\n",
            "[63 63 63 ... 63 63 63]\n",
            "[Epoch   7/100] train_loss: 13712.67676\n",
            "[63 63 63 ... 63 63 63]\n",
            "[Epoch   8/100] train_loss: 13667.46680\n",
            "[63 63 63 ... 63 63 63]\n",
            "[Epoch   9/100] train_loss: 13595.87500\n",
            "[63 63 63 ... 63 63 63]\n",
            "[Epoch  10/100] train_loss: 13511.95996\n",
            "[63 63 63 ... 63 63 63]\n",
            "[Epoch  11/100] train_loss: 13500.74609\n",
            "[63 63 63 ... 63 63 63]\n",
            "[Epoch  12/100] train_loss: 13480.24316\n",
            "[63 63 63 ... 63 63 63]\n",
            "[Epoch  13/100] train_loss: 13638.92969\n",
            "[63 63 63 ... 63 63 63]\n",
            "[Epoch  14/100] train_loss: 13559.65137\n",
            "[63 63 63 ... 63 63 63]\n",
            "[Epoch  15/100] train_loss: 13746.86230\n",
            "[63 63 63 ... 63 63 63]\n",
            "[Epoch  16/100] train_loss: 13757.27930\n",
            "[63 63 63 ... 63 63 63]\n",
            "[Epoch  17/100] train_loss: 13376.75391\n",
            "[63 63 63 ... 63 63 63]\n",
            "[Epoch  18/100] train_loss: 13367.62500\n",
            "[63 63 63 ... 63 63 63]\n",
            "[Epoch  19/100] train_loss: 13661.18750\n",
            "[63 63 63 ... 63 63 63]\n",
            "[Epoch  20/100] train_loss: 13686.85645\n",
            "[63 63 63 ... 63 63 63]\n",
            "[Epoch  21/100] train_loss: 13773.26074\n",
            "[63 63 63 ... 63 63 63]\n",
            "[Epoch  22/100] train_loss: 13773.57227\n",
            "[63 63 63 ... 63 63 63]\n",
            "[Epoch  23/100] train_loss: 13706.97949\n",
            "[63 63 63 ... 63 63 63]\n",
            "[Epoch  24/100] train_loss: 13353.34863\n",
            "[63 63 63 ... 63 63 63]\n",
            "[Epoch  25/100] train_loss: 13353.08496\n",
            "[63 63 63 ... 63 63 63]\n",
            "[Epoch  26/100] train_loss: 13759.57910\n",
            "[63 63 63 ... 63 63 63]\n",
            "[Epoch  27/100] train_loss: 13773.80566\n",
            "[63 63 63 ... 63 63 63]\n",
            "[Epoch  28/100] train_loss: 13773.72754\n",
            "[63 63 63 ... 63 63 63]\n",
            "[Epoch  29/100] train_loss: 13355.85645\n",
            "[63 63 63 ... 63 63 63]\n",
            "[Epoch  30/100] train_loss: 13758.00391\n",
            "[63 63 63 ... 63 63 63]\n",
            "[Epoch  31/100] train_loss: 13772.07031\n",
            "[63 63 63 ... 63 63 63]\n",
            "[Epoch  32/100] train_loss: 13771.94336\n",
            "[63 63 63 ... 63 63 63]\n",
            "[Epoch  33/100] train_loss: 13756.92871\n",
            "[63 63 63 ... 63 63 63]\n",
            "[Epoch  34/100] train_loss: 13756.19531\n",
            "[63 63 63 ... 63 63 63]\n",
            "[Epoch  35/100] train_loss: 13769.70312\n",
            "[63 63 63 ... 63 63 63]\n",
            "[Epoch  36/100] train_loss: 13753.78906\n",
            "[63 63 63 ... 63 63 63]\n",
            "[Epoch  37/100] train_loss: 13566.81445\n",
            "[63 63 63 ... 63 63 63]\n",
            "[Epoch  38/100] train_loss: 13750.95020\n",
            "[63 63 63 ... 63 63 63]\n",
            "[Epoch  39/100] train_loss: 13767.57227\n",
            "[63 63 63 ... 63 63 63]\n",
            "[Epoch  40/100] train_loss: 13750.12598\n",
            "[63 63 63 ... 63 63 63]\n",
            "[Epoch  41/100] train_loss: 13636.46094\n",
            "[71 63 63 ... 63 63 63]\n",
            "[Epoch  42/100] train_loss: 13625.87891\n",
            "[71 71 71 ... 71 71 71]\n",
            "[Epoch  43/100] train_loss: 13768.55176\n",
            "[71 71 71 ... 71 71 71]\n",
            "[Epoch  44/100] train_loss: 13769.46094\n",
            "[71 71 71 ... 71 71 71]\n",
            "[Epoch  45/100] train_loss: 13751.13086\n",
            "[71 71 71 ... 71 71 71]\n",
            "[Epoch  46/100] train_loss: 13772.26562\n",
            "[71 71 71 ... 71 71 71]\n",
            "[Epoch  47/100] train_loss: 13491.66504\n",
            "[71 71 71 ... 71 71 71]\n",
            "[Epoch  48/100] train_loss: 13570.36133\n",
            "[71 71 71 ... 71 71 71]\n",
            "[Epoch  49/100] train_loss: 13475.65918\n",
            "[71 71 71 ... 71 71 71]\n",
            "[Epoch  50/100] train_loss: 13471.45410\n",
            "[71 71 71 ... 71 71 71]\n",
            "[Epoch  51/100] train_loss: 13527.58496\n",
            "[71 71 71 ... 71 71 71]\n",
            "[Epoch  52/100] train_loss: 12281.12305\n",
            "[71 71 71 ... 71 71 71]\n",
            "[Epoch  53/100] train_loss: 13530.87988\n",
            "[71 71 71 ... 71 71 71]\n",
            "[Epoch  54/100] train_loss: 13756.40723\n",
            "[71 71 71 ... 71 71 71]\n",
            "[Epoch  55/100] train_loss: 13463.08594\n",
            "[71 71 71 ... 71 71 71]\n",
            "[Epoch  56/100] train_loss: 13774.09180\n",
            "[71 71 71 ... 71 71 71]\n",
            "[Epoch  57/100] train_loss: 13756.40527\n",
            "[71 71 71 ... 71 71 71]\n",
            "[Epoch  58/100] train_loss: 13778.49805\n",
            "[71 71 71 ... 71 71 71]\n",
            "[Epoch  59/100] train_loss: 13756.50000\n",
            "[71 71 71 ... 71 71 71]\n",
            "[Epoch  60/100] train_loss: 13778.49805\n",
            "[71 71 71 ... 71 71 71]\n",
            "[Epoch  61/100] train_loss: 13774.48535\n",
            "[71 71 71 ... 71 71 71]\n",
            "[Epoch  62/100] train_loss: 13462.50000\n",
            "[71 71 71 ... 71 71 71]\n",
            "[Epoch  63/100] train_loss: 13778.49902\n",
            "[71 71 71 ... 71 71 71]\n",
            "[Epoch  64/100] train_loss: 13778.49902\n",
            "[71 71 71 ... 71 71 71]\n",
            "[Epoch  65/100] train_loss: 12260.51562\n",
            "[71 71 71 ... 71 71 71]\n",
            "[Epoch  66/100] train_loss: 13462.50293\n",
            "[71 71 71 ... 71 71 71]\n",
            "[Epoch  67/100] train_loss: 13778.49902\n",
            "[71 71 71 ... 71 71 71]\n",
            "[Epoch  68/100] train_loss: 13778.49902\n",
            "[71 71 71 ... 71 71 71]\n",
            "[Epoch  69/100] train_loss: 13557.50293\n",
            "[71 71 71 ... 71 71 71]\n",
            "[Epoch  70/100] train_loss: 13756.49902\n",
            "[71 71 71 ... 71 71 71]\n",
            "[Epoch  71/100] train_loss: 13778.49902\n",
            "[71 71 71 ... 71 71 71]\n",
            "[Epoch  72/100] train_loss: 13778.49902\n",
            "[71 71 71 ... 71 71 71]\n",
            "[Epoch  73/100] train_loss: 13774.49902\n",
            "[71 71 71 ... 71 71 71]\n",
            "[Epoch  74/100] train_loss: 13532.49902\n",
            "[71 71 71 ... 71 71 71]\n",
            "[Epoch  75/100] train_loss: 13778.49902\n",
            "[71 71 71 ... 71 71 71]\n",
            "[Epoch  76/100] train_loss: 13462.50293\n",
            "[71 71 71 ... 71 71 71]\n",
            "[Epoch  77/100] train_loss: 13778.49902\n",
            "[71 71 71 ... 71 71 71]\n",
            "[Epoch  78/100] train_loss: 13557.50293\n",
            "[71 71 71 ... 71 71 71]\n",
            "[Epoch  79/100] train_loss: 13557.50293\n",
            "[71 71 71 ... 71 71 71]\n",
            "[Epoch  80/100] train_loss: 12260.51562\n",
            "[71 71 71 ... 71 71 71]\n",
            "[Epoch  81/100] train_loss: 13774.49902\n",
            "[71 71 71 ... 71 71 71]\n",
            "[Epoch  82/100] train_loss: 13778.49902\n",
            "[71 71 71 ... 71 71 71]\n",
            "[Epoch  83/100] train_loss: 13756.49902\n",
            "[71 71 71 ... 71 71 71]\n",
            "[Epoch  84/100] train_loss: 13557.50293\n",
            "[71 71 71 ... 71 71 71]\n",
            "[Epoch  85/100] train_loss: 13774.49902\n",
            "[71 71 71 ... 71 71 71]\n",
            "[Epoch  86/100] train_loss: 12260.51562\n",
            "[71 71 71 ... 71 71 71]\n",
            "[Epoch  87/100] train_loss: 13532.49902\n",
            "[71 71 71 ... 71 71 71]\n",
            "[Epoch  88/100] train_loss: 13778.49902\n",
            "[71 71 71 ... 71 71 71]\n",
            "[Epoch  89/100] train_loss: 13756.49902\n",
            "[71 71 71 ... 71 71 71]\n",
            "[Epoch  90/100] train_loss: 12260.51562\n",
            "[71 71 71 ... 71 71 71]\n",
            "[Epoch  91/100] train_loss: 13462.50293\n",
            "[71 71 71 ... 71 71 71]\n",
            "[Epoch  92/100] train_loss: 13557.50293\n",
            "[71 71 71 ... 71 71 71]\n",
            "[Epoch  93/100] train_loss: 13462.50293\n",
            "[71 71 71 ... 71 71 71]\n",
            "[Epoch  94/100] train_loss: 13756.49902\n",
            "[71 71 71 ... 71 71 71]\n",
            "[Epoch  95/100] train_loss: 13778.49902\n",
            "[71 71 71 ... 71 71 71]\n",
            "[Epoch  96/100] train_loss: 13774.49902\n",
            "[71 71 71 ... 71 71 71]\n",
            "[Epoch  97/100] train_loss: 13778.49902\n",
            "[71 71 71 ... 71 71 71]\n",
            "[Epoch  98/100] train_loss: 13778.49902\n",
            "[71 71 71 ... 71 71 71]\n",
            "[Epoch  99/100] train_loss: 13778.49902\n",
            "[71 71 71 ... 71 71 71]\n",
            "[Epoch 100/100] train_loss: 12260.51562\n",
            "[71 71 71 ... 71 71 71]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "87Pu4uJbWtYA",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 140
        },
        "outputId": "e8b01b88-aea0-4d57-e8ef-330579e9497d"
      },
      "source": [
        "\n",
        "outputdata = np.zeros((128,2832)) #出力を格納する行列\n",
        "for t in range(2832):\n",
        "  outputdata[seq[t],t] = 90　#音量を決定\n",
        "\n",
        "print(outputdata)\n",
        "outputdata = np.transpose(outputdata)"
      ],
      "execution_count": 41,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[[0. 0. 0. ... 0. 0. 0.]\n",
            " [0. 0. 0. ... 0. 0. 0.]\n",
            " [0. 0. 0. ... 0. 0. 0.]\n",
            " ...\n",
            " [0. 0. 0. ... 0. 0. 0.]\n",
            " [0. 0. 0. ... 0. 0. 0.]\n",
            " [0. 0. 0. ... 0. 0. 0.]]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "vcFjEpgB6xLe",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "multi = pypianoroll.Multitrack()"
      ],
      "execution_count": 42,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "N4u1FSveVMEj",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "bbba9fc2-503a-4b78-f5bd-08089370a293"
      },
      "source": [
        "track = Track(pianoroll=outputdata, program=0, is_drum=False,name='my awesome piano')\n",
        "print(track.pianoroll.ndim)"
      ],
      "execution_count": 43,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "2\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "4WBfyHyGVSB9",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "another_track = track.copy()"
      ],
      "execution_count": 44,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "0bi6NRT3VS-T",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "multitrack = Multitrack(tracks=[track, another_track], tempo=120.0)"
      ],
      "execution_count": 45,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "NpI-eJx1VWdr",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "multitrack.write(\"create1.mid\")"
      ],
      "execution_count": 46,
      "outputs": []
    }
  ]
}