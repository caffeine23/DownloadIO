import {
  Input,
  Radio,
  RadioGroup,
  Stack,
  Button,
  Spinner,
} from "@chakra-ui/react";
import { useState } from "react";
import { FaDownload, FaCheck } from "react-icons/fa";
import axios from "axios";

export default function LinkInput({ site }) {
  const [link, setLink] = useState("");
  const [type, setType] = useState("video");
  const [isSubmitted, setIsSubmitted] = useState(false);
  const [isDownloadReady, setIsDownloadReady] = useState(false);
  const [fileBlob, setFileBlob] = useState(null);
  const [filename, setFilename] = useState("");

  function handleSubmit(evt) {
    evt.preventDefault();
    setIsDownloadReady(false);
    setIsSubmitted(true);
    try {
      axios
        .get(`/download/${site}?url=${link}&type=${type}`, {
          responseType: "blob",
        })
        .then((response) => {
          const url = window.URL.createObjectURL(new Blob([response.data]));
          const filename = type === "video" ? "download.mp4" : "download.mp3";
          setFileBlob(url);
          setFilename(filename);
          setIsDownloadReady(true);
        });
    } catch (err) {
      console.log(err);
    }
  }

  function handleDownload() {
    const link = document.createElement("a");
    link.href = fileBlob;
    link.setAttribute("download", filename);
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  }

  return (
    <form onSubmit={handleSubmit}>
      <Stack>
        <Stack spacing={10} direction="row" className="mt-12 mx-8">
          <Input
            variant="flushed"
            placeholder="Enter video URL"
            value={link}
            onChange={(evt) => {
              setLink(evt.target.value);
            }}
          />
          <RadioGroup defaultValue="video" onChange={setType}>
            <Radio colorScheme="green" value="video">
              MP4
            </Radio>
            <Radio colorScheme="green" value="audio">
              MP3
            </Radio>
          </RadioGroup>
          <Button
            rightIcon={<FaCheck />}
            colorScheme="green"
            size="md"
            type="submit"
          >
            Submit
          </Button>
        </Stack>
        {isSubmitted ? (
          <div className="flex justify-center mt-4">
            {isDownloadReady ? (
              <Button colorScheme="blue" size="lg" onClick={handleDownload}>
                <FaDownload className="mr-2" />
                Download
              </Button>
            ) : (
              <Spinner size="lg" />
            )}
          </div>
        ) : null}
      </Stack>
    </form>
  );
}
