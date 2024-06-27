import { Tabs, TabList, TabPanels, Tab, TabPanel } from "@chakra-ui/react";
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
          <Tab>Instagram</Tab>
          <Tab>YouTube</Tab>
          <Tab>Reddit</Tab>
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
