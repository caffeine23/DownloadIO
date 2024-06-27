import { Tabs, TabList, TabPanels, Tab, TabPanel } from "@chakra-ui/react";
import { FaInstagram, FaYoutube, FaReddit } from "react-icons/fa";

import LinkInput from "./LinkInput";

export default function WebsitePicker() {
  return (
    <>
      <Tabs
        variant="enclosed-colored"
        colorScheme="green"
        isFitted
        defaultIndex={1}
        className="mt-4"
      >
        <TabList>
          <Tab>
            Instagram <FaInstagram className="ml-2" />
          </Tab>
          <Tab>
            YouTube <FaYoutube className="ml-2" />
          </Tab>
          <Tab>
            Reddit <FaReddit className="ml-2" />
          </Tab>
        </TabList>

        <TabPanels>
          <TabPanel>
            <LinkInput site="instagram" />
          </TabPanel>
          <TabPanel>
            <LinkInput site="youtube" />
          </TabPanel>
          <TabPanel>
            <LinkInput site="reddit" />
          </TabPanel>
        </TabPanels>
      </Tabs>
    </>
  );
}
